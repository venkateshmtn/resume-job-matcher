from langchain_community.document_loaders import PyPDFLoader
import tempfile

def load_pdf(uploaded_file):
    # Save uploaded file to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Load using file path
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    return documents