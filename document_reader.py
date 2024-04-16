# document_reader.py
import PyPDF2
import docx

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = [page.extract_text() for page in reader.pages if page.extract_text()]
        return " ".join(text)

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = [paragraph.text for paragraph in doc.paragraphs if paragraph.text]
    return " ".join(text)
