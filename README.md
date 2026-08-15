# Medical RAG

## Overview

Medical RAG is a medical question-answering system that uses Retrieval-Augmented Generation (RAG) to provide context-based responses to questions about diseases and symptoms.

The system uses medical documents collected from sources such as the World Health Organization (WHO). Users can enter a medical question or symptoms through a web interface, and the system retrieves relevant information from the medical knowledge base before generating a response using a locally running language model.

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### RAG / AI
- Retrieval-Augmented Generation (RAG)
- BAAI BGE-small-en-v1.5 — Embedding Model
- ChromaDB — Vector Database
- Microsoft Phi-2 — Large Language Model (LLM)

### Document Processing
- PDF document extraction
- Text chunking
- Vector embeddings

## RAG Components

| Component | Purpose |
|---|---|
| Medical Documents | Provide the knowledge base for the system |
| Text Chunking | Splits medical documents into smaller sections |
| BGE-small-en-v1.5 | Converts text into vector embeddings |
| ChromaDB | Stores embeddings and performs similarity search |
| Retrieval | Retrieves the most relevant document chunks |
| Microsoft Phi-2 | Generates the final response using retrieved context |
| FastAPI | Connects the frontend with the RAG pipeline |

## Architecture

```text
                  User
                   |
                   v
          HTML / CSS / JavaScript
                   |
                   | HTTP POST
                   v
                FastAPI
                   |
                   v
              User Query
                   |
                   v
        BGE-small-en-v1.5
          Query Embedding
                   |
                   v
               ChromaDB
          Similarity Search
                   |
                   v
          Relevant Chunks
                   |
                   v
        Query + Retrieved Context
                   |
                   v
          Microsoft Phi-2
                   |
                   v
            Final Answer
                   |
                   v
              FastAPI
                   |
                   v
              Frontend
