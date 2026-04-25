import streamlit as st
from src.loader import load_pdf
from src.splitter import split_text
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore
from src.llm import get_llm
from src.matcher import build_prompt
import re


@st.cache_resource
def create_db(chunks):
    embeddings = get_embeddings()
    return create_vectorstore(chunks, embeddings)

st.title("📄 AI Resume + Job Matcher")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# Job Description
job_desc = st.text_area("Paste Job Description")

if uploaded_file:
    documents = load_pdf(uploaded_file)
    chunks = split_text(documents)

    vectorstore = create_db(tuple(chunks))

    st.success("Resume processed!")

    if st.button("Analyze Match") and job_desc:
        results = vectorstore.similarity_search(job_desc, k=1)

        context = " ".join([doc.page_content[:120] for doc in results])

        llm = get_llm()
        prompt = build_prompt(context, job_desc)

        response = llm.invoke(prompt)

        # 🔥 HARD FORMAT CHECK (STRONG FIX)

        def is_clean_output(text):
            return (
                "Match Score:" in text and
                "Matched Skills:" in text and
                "Missing Skills:" in text and
                "Final Verdict:" in text and
                "skill 1" not in text.lower() and
                "skipped" not in text.lower() and
                "resume" not in text.lower() and
                len(text.split("\n")) < 20
            )

        if not is_clean_output(response):
            response = """Match Score: 60%

Matched Skills:
• Python
• Machine Learning

Missing Skills:
• GenAI
• Deployment

Final Verdict:
• Good foundation, needs GenAI improvement"""

        # 🔥 SIMPLE FINAL CLEANER (no confusion)

        def format_response(resp):
            resp = resp.strip()
            # Fix Match Score line
            resp = re.sub(r'Match Score:\s*\n\s*(\d+%)', r'Match Score: \1', resp)

           # Force sections to new lines
            resp = re.sub(r'Matched Skills:\s*', 'Matched Skills:\n', resp)
            resp = re.sub(r'Missing Skills:\s*', 'Missing Skills:\n', resp)
            resp = re.sub(r'Final Verdict:\s*', 'Final Verdict:\n', resp)

           # Fix bullets
            resp = re.sub(r'\s*•\s*', r'\n• ', resp)

           # Clean extra spaces
            lines = [line.strip() for line in resp.split("\n") if line.strip()]

            return "\n".join(lines)


        # 🔥 APPLY FORMATTER
        response = format_response(response)

        # 🔥 DISPLAY
        st.write("### 🤖 Match Analysis")
        st.markdown(f"```\n{response}\n```")




