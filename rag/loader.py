from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


DOCUMENTS_DIR = Path("rag/documents")


def load_documents():

    documents = []

    pdf_files = DOCUMENTS_DIR.glob("*.pdf")

    for pdf in pdf_files:

        loader = PyPDFLoader(str(pdf))

        documents.extend(loader.load())

    return documents