```
# 🎥 YouTube Chatbot using LangChain

> An AI-powered YouTube chatbot that allows users to ask questions about YouTube videos using **Retrieval-Augmented Generation (RAG)**, **LangChain**, **Google Gemini**, and **FAISS**.

---

## 📌 Overview

The **YouTube Chatbot** is a RAG-based application that lets users interact with the content of a YouTube video through natural-language questions.

Instead of sending the complete transcript to the Large Language Model, the application:

1. Extracts the YouTube transcript
2. Splits the transcript into smaller chunks
3. Converts the chunks into vector embeddings
4. Stores the embeddings in a FAISS vector database
5. Retrieves the most relevant chunks for a user's question
6. Passes the retrieved context to Google Gemini
7. Generates a context-aware answer

The application provides an interactive interface using **Streamlit**.

---

## 💡 Why I Built This

I built this project to understand how **Retrieval-Augmented Generation (RAG)** works in a practical application.

While learning LangChain and Generative AI, I wanted to build something where an LLM could answer questions based on a specific source of information rather than relying only on its pretrained knowledge.

This project helped me understand:

- Document loading
- Text chunking
- Embeddings
- Vector databases
- Semantic similarity search
- Retrieval
- Prompt engineering
- RAG pipelines
- LLM-based answer generation
- Streamlit application development

---

## ✨ Features

- 🎥 Accepts YouTube video URLs
- 📝 Extracts YouTube video transcripts
- ✂️ Splits transcripts into manageable chunks
- 🧠 Generates embeddings using Google Gemini
- 🗄️ Stores embeddings using FAISS
- 🔍 Retrieves relevant transcript chunks
- 🤖 Generates answers using Google Gemini
- 🔗 Uses LangChain for the RAG pipeline
- 💬 Interactive Streamlit interface
- 🔐 API keys are managed using environment variables

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   YouTube Video     │
                    │       URL           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Extract Video ID    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ YouTube Transcript  │
                    │       API           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ LangChain Document  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Text Splitting    │
                    │   Chunk + Overlap   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Gemini Embeddings   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FAISS Vector      │
                    │       Store         │
                    └──────────┬──────────┘
                               │
                               │
                     USER QUESTION
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Retriever       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Relevant Context    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  LangChain RAG      │
                    │      Chain          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Google Gemini     │
                    │       LLM           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   AI Generated      │
                    │      Answer         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    └─────────────────────┘
```

---

## 🔄 RAG Pipeline

The core RAG pipeline works as follows:

```text
YouTube Transcript
        ↓
Document Creation
        ↓
Text Chunking
        ↓
Embeddings
        ↓
FAISS Vector Store
        ↓
Similarity Search
        ↓
Relevant Context
        ↓
Prompt + Context
        ↓
Google Gemini
        ↓
Generated Answer
```

---

## 🧠 How It Works

### 1. YouTube URL

The user enters a YouTube video URL through the Streamlit interface.

### 2. Video ID Extraction

The application extracts the unique YouTube video ID from the URL.

### 3. Transcript Extraction

The YouTube Transcript API is used to retrieve the available transcript.

### 4. Document Creation

The transcript is converted into a LangChain `Document`.

### 5. Text Splitting

The transcript is divided into smaller chunks using:

```python
RecursiveCharacterTextSplitter
```

Chunking makes retrieval more efficient and allows the model to work with relevant portions of the transcript.

### 6. Embeddings

Each text chunk is converted into a numerical vector using Google Gemini embeddings.

```text
Text
 ↓
Embedding Model
 ↓
Vector Representation
```

### 7. FAISS Vector Store

The generated vectors are stored in a FAISS vector database.

FAISS allows the application to efficiently search for semantically similar content.

### 8. Retrieval

When the user asks a question, the retriever searches the vector database and returns the most relevant transcript chunks.

### 9. RAG

The retrieved chunks are added to the prompt as context.

The LLM receives:

```text
User Question
      +
Retrieved Context
      ↓
Google Gemini
      ↓
Answer
```

### 10. Answer Generation

Google Gemini generates the final answer using the retrieved transcript context.

---

## 🧠 Technical Decisions

### Why RAG?

A YouTube video can contain a large amount of information.

Instead of sending the entire transcript to the LLM for every question, RAG retrieves only the relevant information.

This helps make the application more efficient and keeps the generated answers grounded in the video transcript.

### Why FAISS?

FAISS provides efficient similarity search over vector embeddings and is simple to integrate into a local RAG application.

### Why LangChain?

LangChain provides useful abstractions for:

- Documents
- Text splitters
- Retrievers
- Prompts
- LLMs
- RAG pipelines

This makes it easier to connect the different components of the application.

### Why Google Gemini?

Google Gemini is used for both:

- Text generation
- Embeddings

This provides a consistent Google AI stack for the application.

### Why Streamlit?

Streamlit provides a simple way to turn the Python-based RAG pipeline into an interactive web application without requiring a separate frontend framework.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangChain | RAG and LLM application framework |
| Google Gemini | LLM and embeddings |
| FAISS | Vector similarity search |
| YouTube Transcript API | Transcript extraction |
| Streamlit | Web interface |
| python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
Youtube-chatbot-LangChain/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

> `.env` is intentionally excluded from the repository for security reasons.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yashu1905-bit/Youtube-chatbot-LangChain.git
```

### 2. Navigate into the project

```bash
cd Youtube-chatbot-LangChain
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You can use `.env.example` as a reference.

### ⚠️ Security

Never commit your actual API key to GitHub.

The `.env` file is included in `.gitignore`.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Questions

After loading a YouTube video, you can ask questions such as:

```text
What is this video about?

What are the main concepts discussed in the video?

Explain the main topic in simple words.

What are the key points mentioned in the video?

What problem is being discussed?

Can you summarize the important points?

Explain the concept discussed in the video with an example.
```

---

## 📸 Application Screenshots

### YouTube Chatbot Interface

Add your Streamlit application screenshot here.

### RAG Architecture

Add the architecture diagram here.

> Screenshots are included to demonstrate the working application and the overall RAG pipeline.

---

## 🧪 Example Workflow

```text
1. Open the application
        ↓
2. Enter YouTube URL
        ↓
3. Click "Load Video"
        ↓
4. Transcript is extracted
        ↓
5. Transcript is chunked
        ↓
6. Embeddings are generated
        ↓
7. FAISS index is created
        ↓
8. Ask a question
        ↓
9. Relevant chunks are retrieved
        ↓
10. Gemini generates the answer
```

---

## ⚠️ Limitations

- The application depends on the availability of a YouTube transcript.
- Videos without accessible transcripts cannot be processed.
- FAISS is currently used as a local vector store.
- The quality of answers depends on the quality and completeness of the transcript.
- The current version processes one video at a time.
- Conversation history is not yet persistent.

---

## 🔮 Future Improvements

The project can be extended with:

- [ ] 💬 Persistent chat history
- [ ] 🎥 Support for multiple YouTube videos
- [ ] 📑 Automatic video summarization
- [ ] ⏱️ Timestamp-based answers
- [ ] 🔗 Source citations
- [ ] 🧠 Conversation memory
- [ ] 🌐 Multilingual transcript support
- [ ] 🎨 Improved UI/UX
- [ ] ☁️ Cloud deployment
- [ ] 🔐 User authentication
- [ ] 🗄️ Production vector database
- [ ] 📊 Retrieval evaluation
- [ ] ⚡ Streaming LLM responses

---

## 📈 Learning Outcomes

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation
- LangChain
- LLM integration
- Vector embeddings
- FAISS
- Semantic search
- Prompt engineering
- Document processing
- Streamlit
- Environment variable management
- Building an end-to-end Generative AI application

---

## 👨‍💻 Author

### Yashu

B.Tech Computer Engineering

GitHub:  
https://github.com/yashu1905-bit

---

## ⭐ Feedback

If you find this project useful or have suggestions for improvement, feel free to open an issue or contribute to the project.

If you like the project, consider giving it a ⭐.

---

## 📄 License

This project is intended for educational and portfolio purposes.   



<img width="821" height="827" alt="Screenshot 2026-10-04 185313" src="https://github.com/user-attachments/assets/661c993a-cbc3-46da-b58e-a34f363747bf" />
<img width="887" height="691" alt="Screenshot 2026-10-04 185330" src="https://github.com/user-attachments/assets/145ffec5-cb2f-49c8-94f5-938cfdc660ba" />
<img width="1920" height="1080" alt="Screenshot (604)" src="https://github.com/user-attachments/assets/ecb387b2-84d1-4f9f-b864-2e008aea64ad" />


