import os
import re
import streamlit as st

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

st.set_page_config(
    page_title="YouTube Chatbot",
    page_icon="🎥"
)

st.title("🎥 YouTube Chatbot")
st.write("Ask questions about any YouTube video.")


# -----------------------------
# YouTube Video ID
# -----------------------------

def get_video_id(url):

    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be\/([0-9A-Za-z_-]{11})"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)

        if match:
            return match.group(1)

    return None


# -----------------------------
# Load Transcript
# -----------------------------

def load_transcript(video_id):

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join(
        snippet.text for snippet in transcript
    )

    return text


# -----------------------------
# Create Vector Store
# -----------------------------

def create_vector_store(text):

    document = Document(
        page_content=text
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        [document]
    )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


# -----------------------------
# LLM
# -----------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# -----------------------------
# Prompt
# -----------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful YouTube video assistant.

Answer the user's question ONLY using the provided
video transcript.

If the answer is not present in the transcript,
say:

"I couldn't find the answer in this video."

Transcript:
{context}

Question:
{question}

Answer:
"""
)


# -----------------------------
# Session State
# -----------------------------

if "vectorstore" not in st.session_state:

    st.session_state.vectorstore = None


# -----------------------------
# YouTube URL
# -----------------------------

youtube_url = st.text_input(
    "🔗 Enter YouTube URL"
)


# -----------------------------
# Load Video
# -----------------------------

if st.button("Load Video"):

    if not youtube_url:

        st.warning("Please enter a YouTube URL.")

    else:

        video_id = get_video_id(
            youtube_url
        )

        if not video_id:

            st.error("Invalid YouTube URL.")

        else:

            with st.spinner(
                "Loading YouTube transcript..."
            ):

                try:

                    text = load_transcript(
                        video_id
                    )

                    st.success(
                        "Transcript loaded successfully!"
                    )

                    with st.spinner(
                        "Creating vector database..."
                    ):

                        vectorstore = create_vector_store(
                            text
                        )

                        st.session_state.vectorstore = vectorstore

                    st.success(
                        "Video is ready! Ask your question below."
                    )

                except Exception as e:

                    st.error(
                        f"Error: {e}"
                    )


# -----------------------------
# Question
# -----------------------------

question = st.text_input(
    "💬 Ask a question about the video"
)


if st.button("Ask"):

    if st.session_state.vectorstore is None:

        st.warning(
            "First load a YouTube video."
        )

    elif not question:

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner("Thinking..."):

            retriever = (
                st.session_state
                .vectorstore
                .as_retriever(
                    search_kwargs={
                        "k": 4
                    }
                )
            )

            docs = retriever.invoke(
                question
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            chain = (
                prompt
                | model
                | StrOutputParser()
            )

            answer = chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            st.markdown("### 🤖 Answer")

            st.write(answer)