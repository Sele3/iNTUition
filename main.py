from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from summarizer import text_summarizer
import re

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/uploadfile/")
async def create_upload_file(file: UploadFile):
    text = extract_pdf_file(file.file)
    summarized = text_summarizer(text)
    print(summarized)
    
    return {"filename": file.filename}


def extract_pdf_file(file) -> str:
    pdf_reader : PdfReader = PdfReader(file)
    
    text = ""
    with open('sample.txt', 'w', encoding='utf-8') as f:
        for page_num in range(1, len(pdf_reader.pages)):
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
    # Remove text within square or round brackets
    s = re.sub(r'[\[\(].*?[\]\)]', '', s)
    # Replace hyphens with space
    s = re.sub(r' - ', '', s)
    # # Remove numbers and numbers with symbols within
    # s = re.sub(r'\b\w*[\d,]+\w*\b', '', s)
    # Remove extra white spaces
    s = re.sub(r'\s\s+', ' ', s)

    return s
