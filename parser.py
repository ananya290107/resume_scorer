import pdfplumber
from docx import Document


def parse_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def parse_docx(path):
    doc = Document(path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text
