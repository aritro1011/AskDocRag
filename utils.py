import pdfplumber
from docx import Document

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_file):
    text = ""
    
    # Use pdfplumber to open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Iterate over all pages and extract text
        for page in pdf.pages:
            text += page.extract_text()

    return text

# Function to extract text from DOCX using python-docx
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""

    # Loop through each paragraph and concatenate the text
    for para in doc.paragraphs:
        text += para.text + "\n"

    return text
