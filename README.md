# 🎥 YouTube Chatbot using LangChain

An AI-powered YouTube chatbot that allows users to ask questions about YouTube videos. The application extracts the video's transcript, processes it using LangChain, stores semantic embeddings in FAISS, and uses Google Gemini to generate context-aware answers.

## 🚀 Features

- 🎥 Accepts YouTube video URLs
- 📝 Automatically extracts YouTube transcripts
- ✂️ Splits transcripts into smaller chunks
- 🧠 Generates semantic embeddings using Gemini
- 🔍 Performs similarity search using FAISS
- 🤖 Uses Google Gemini for answer generation
- 🔗 Built using LangChain RAG architecture
- 💬 Interactive Streamlit interface
- ⚡ Fast context-based question answering

## 🏗️ Architecture

```text
YouTube URL
     │
     ▼
Extract Video ID
     │
     ▼
YouTube Transcript
     │
     ▼
LangChain Document
     │
     ▼
Text Splitting
     │
     ▼
Gemini Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Retriever
     │
     ▼
Relevant Context
     │
     ▼
LangChain RAG Chain
     │
     ▼
Google Gemini
     │
     ▼
AI Generated Answer
     │
     ▼
Streamlit UI    



<img width="821" height="827" alt="Screenshot 2026-10-04 185313" src="https://github.com/user-attachments/assets/661c993a-cbc3-46da-b58e-a34f363747bf" />
<img width="887" height="691" alt="Screenshot 2026-10-04 185330" src="https://github.com/user-attachments/assets/145ffec5-cb2f-49c8-94f5-938cfdc660ba" />
<img width="1920" height="1080" alt="Screenshot (604)" src="https://github.com/user-attachments/assets/ecb387b2-84d1-4f9f-b864-2e008aea64ad" />


