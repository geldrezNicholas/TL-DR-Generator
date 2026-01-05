# PyTorch TL;DR Generator 📚

A custom NLP web application built with PyTorch, Hugging Face Transformers, and Streamlit. This tool uses the BART architecture to generate summaries of text or uploaded files.

## 🚀 Features
- **Smart Summarization:** Uses `facebook/bart-large-cnn` to rewrite text concisely.
- **Custom Controls:** Adjust minimum and maximum summary length via the sidebar.
- **Dual Input:** Accepts both pasted text and `.txt` file uploads.
- **Export:** Download generated summaries instantly.

## 🛠️ How to Run
1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```   
2. **How to run:**
   ```bash
   streamlit run app.py
   ```

## 🎓 Learning & Attribution
Built as a learning tutorial to understand PyTorch by manually implementing `BartForConditionalGeneration`, focusing on low-level tensor manipulation instead of using pre-built pipelines.
