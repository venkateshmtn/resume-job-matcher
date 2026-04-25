# 📄 AI Resume + Job Matcher

🚀 An end-to-end AI-powered application that analyzes resumes against job descriptions using LLMs and Retrieval-Augmented Generation (RAG).

---

## 🔍 Overview

The **AI Resume + Job Matcher** helps evaluate how well a candidate's resume aligns with a job description.
It leverages **semantic search (FAISS)** and **LLM reasoning** to generate a structured match analysis including:

* Match Score
* Matched Skills
* Missing Skills
* Final Verdict

---

## ⚙️ Features

* 📄 Upload resume in PDF format
* 🧠 Extract and process text using document loaders
* 🔍 Semantic search using FAISS vector database
* 🤖 LLM-powered analysis for intelligent matching
* 📊 Structured and concise output format
* ⚡ Streamlit-based interactive UI

---

## 🏗️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **LangChain**
* **FAISS** (Vector Database)
* **LLMs (Ollama / Local Models)**
* **PyPDF Loader**

---

## 🧠 How It Works

1. Upload Resume (PDF)
2. Paste Job Description
3. Resume is split into chunks
4. Embeddings are generated
5. FAISS performs similarity search
6. Relevant context is passed to LLM
7. LLM generates structured match analysis

---

## 📂 Project Structure

```
resume-job-matcher/
│── app.py
│── requirements.txt
│── .gitignore
│── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── matcher.py
│   └── llm.py
```

---

## 🚀 Installation

```bash
git clone https://github.com/venkateshmtn/resume-job-matcher.git
cd resume-job-matcher
```

### Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📊 Example Output

```
Match Score: 60%

Matched Skills:
• Python
• Machine Learning

Missing Skills:
• GenAI
• Deployment

Final Verdict:
• Good foundation, needs GenAI improvement
```

---

## 🎯 Use Cases

* Resume screening automation
* Job-fit evaluation
* Skill gap analysis
* Career guidance tools

---

## 🚧 Future Improvements

* Real skill scoring (non-LLM logic)
* Multi-resume comparison
* Cloud deployment (AWS/GCP)
* Advanced agent-based workflows

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📬 Contact

**Venkatesh Metan**
🔗 GitHub: https://github.com/venkateshmtn

---

## ⭐ If you found this useful

Give this repo a star ⭐
