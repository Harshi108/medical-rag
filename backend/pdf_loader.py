import fitz
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")


def load_documents():

    documents = {}

    pdf_files = [
        file for file in os.listdir(DATA_FOLDER)
        if file.endswith(".pdf")
    ]

    for pdf in pdf_files:

        pdf_path = os.path.join(DATA_FOLDER, pdf)

        document = fitz.open(pdf_path)

        full_text = ""

        for page in document:
            full_text += page.get_text()

        documents[pdf] = full_text

        document.close()

    return documents