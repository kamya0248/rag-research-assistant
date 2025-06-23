# 📚 RAG for Academic Research Assistance

A Gradio-based web app to help researchers semantically search, summarize, and analyze academic papers.

## 🚀 Features

- 🔍 **Semantic Search** — Retrieve relevant papers based on natural language queries.
- 🌍 **Multilingual Support** — Search and get results in French, German, Spanish, Hindi, and Chinese.
- 📄 **PDF Summarizer** — Upload academic papers and get concise summaries.
- 📈 **Trend Analysis** — Explore trending topics across research papers.
- 🧾 **Citation Generator** — Auto-generate APA citations for papers.

## 📁 File Structure

app/
├── citation_utils.py # Utility for generating APA citations

data/
├── combined_final_papers.csv # Dataset of academic papers

models/
├── bertopic_model/ # Topic modeling saved model
├── semantic_index.faiss # FAISS index for semantic search

notebooks/
├── main.ipynb # Main code
├── [other preprocessing notebooks]

main.py # Final app entry point (converted from main.ipynb)
requirements.txt # Python dependencies
README.md # This file

## 🤖 Built With

- Python
- Gradio
- Sentence Transformers
- HuggingFace Transformers
- BERTopic
- FAISS
- PyMuPDF (for PDF parsing)

## 🌐 Deployment

Hosted on [Hugging Face Spaces](https://huggingface.co/spaces)
