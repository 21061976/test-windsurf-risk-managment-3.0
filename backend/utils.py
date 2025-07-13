import os
from docx import Document
import PyPDF2

def extract_text(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.docx':
        doc = Document(filepath)
        return '\n'.join([p.text for p in doc.paragraphs])
    elif ext == '.pdf':
        text = ''
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ''
        return text
    elif ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise Exception('Unsupported file type')
