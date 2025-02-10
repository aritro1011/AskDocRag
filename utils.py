import pdfplumber
from docx import Document


def extract_text_from_pdf(pdf_file):
    text = ""
    

    with pdfplumber.open(pdf_file) as pdf:
     
        for page in pdf.pages:
            text += page.extract_text()

    return text


def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""

   
    for para in doc.paragraphs:
        text += para.text + "\n"

    return text
