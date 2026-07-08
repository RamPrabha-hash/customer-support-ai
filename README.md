# 🤖 Customer Support AI Agent

An AI-powered customer support system built using **Agentic AI, Retrieval Augmented Generation (RAG), and Large Language Models (LLMs)**. The system can understand customer queries, retrieve relevant information from a knowledge base, maintain conversation context, and automatically escalate complex issues by creating support tickets.

---

# 📌 Project Overview

Traditional customer support systems rely heavily on predefined responses and manual handling. This project introduces an intelligent AI customer support agent that can:

* Understand customer intent
* Search relevant information from a knowledge base
* Generate accurate responses using an LLM
* Remember previous conversation context
* Identify issues requiring human assistance
* Create escalation tickets automatically

The system follows an agent-based architecture where different components work together to provide efficient and personalized customer support.

---

# 🏗️ System Architecture

```
                    Customer
                        |
                        ↓
              Streamlit Frontend
                        |
                        ↓
                FastAPI Backend
                        |
        ┌───────────────┴───────────────┐
        |                               |
        ↓                               ↓
 Intent Router                  Conversation Memory
        |
        ↓
 ┌───────────────┬─────────────────┐
 |               |                 |
 ↓               ↓                 ↓
RAG Agent   Support Agent   Escalation Agent
 |
 ↓
Vector Database
 |
 ↓
OpenRouter LLM
 |
 ↓
Customer Response
```

---

# ✨ Features

## 🔹 AI Chat Support

* Users can ask customer-related questions.
* The AI generates meaningful responses using retrieved information and LLM reasoning.

---

## 🔹 Retrieval Augmented Generation (RAG)

* Uses a knowledge base containing support information.
* Converts documents into embeddings.
* Retrieves the most relevant information using vector similarity search.
* Generates accurate responses based on retrieved context.

---

## 🔹 Intent Detection

The system identifies the customer's requirement and routes the query accordingly.

Examples:

```
Customer:
"What is your refund policy?"

Intent:
Knowledge Query
```

```
Customer:
"I want to talk with an agent."

Intent:
Escalation Request
```

---

## 🔹 Conversation Memory

The AI remembers previous messages during the conversation.

Example:

```
User:
My name is Ram.

User:
What is my name?

AI:
Your name is Ram.
```

---

## 🔹 Automated Ticket Escalation

For complex issues, the system creates a support ticket.

Example:

```
Customer Issue:
Payment failed multiple times

Ticket:
ID: TKT-1201
Priority: HIGH
Status: Open
```

---

## 🔹 LLM Integration

The system uses an external Large Language Model API to generate natural and context-aware responses.

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* Python
* Requests API

## Backend

* FastAPI
* Python
* REST API

## Artificial Intelligence

* LangChain
* Retrieval Augmented Generation (RAG)
* Sentence Transformers
* FAISS Vector Database
* OpenRouter LLM API

## Data Processing

* Document Processing
* Text Embeddings
* Semantic Search

---


# ⚙️ Installation and Setup

## 1. Clone Repository

```bash
git clone <your-github-repository-url>

cd Customer-Support-AI-Agent
```

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

Run FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open another terminal.

Navigate to frontend:

```bash
cd frontend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

Frontend will start at:

```
http://localhost:8501
```

---

# 🔄 Application Workflow

1. Customer enters a query in Streamlit UI.

2. Frontend sends request to FastAPI backend.

3. Backend analyzes user intent.

4. Agent decides the required action:

   * Search knowledge base
   * Retrieve previous conversation context
   * Create escalation ticket

5. Relevant information is retrieved using RAG.

6. OpenRouter LLM generates the final response.

7. Response is displayed to the customer.

---

# 🧠 How RAG Works

```
Documents
    |
    ↓
Text Splitting
    |
    ↓
Embedding Generation
    |
    ↓
Vector Storage
    |
    ↓
User Query
    |
    ↓
Similarity Search
    |
    ↓
Relevant Context
    |
    ↓
LLM Response
```

---

# 🚀 Future Improvements

* Multi-agent workflow using LangGraph
* Customer analytics dashboard
* Voice-based customer support
* Integration with CRM platforms
* Real-time human agent handoff
* Advanced conversation analytics

---

# 🎯 Key Learning Outcomes

Through this project, the following concepts were implemented:

* Building AI-powered applications
* REST API development using FastAPI
* Retrieval Augmented Generation pipelines
* Vector database search
* LLM integration
* Agent-based architecture
* Context-aware chatbot development

---

# 👨‍💻 Author

Ram Prabha

AI / Machine Learning Developer

---

# ⭐ Project Status

✅ Completed
✅ Functional AI Customer Support System
✅ Ready for Deployment
