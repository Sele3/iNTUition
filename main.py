from fastapi import FastAPI, UploadFile
from PyPDF2 import PdfReader
import re

app = FastAPI()


@app.post("/api/uploadfile/")
async def create_upload_file(file: UploadFile):
    extract_pdf_file(file.file)
    
    return {"filename": file.filename}


def extract_pdf_file(file) -> str:
    pdf_reader : PdfReader = PdfReader(file)
    
    text = ""
    with open('sample.txt', 'w', encoding='utf-8') as f:
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
            print('page', page_num, len(text))
            
        text = clean_text(text)
        f.write(text)

    print('done')
    return text


def clean_text(s: str) -> str:
    # Remove newline
    s = s.replace('\n', ' ')
    # Remove 'References' at end of paper
    s = ''.join(s.split('References')[:-1])
    # Remove text within square brackets
    s = re.sub(r'\[.*?\]', '', s)
    # Remove extra white spaces
    s = re.sub(r'\s\s+', ' ', s)

    return s
