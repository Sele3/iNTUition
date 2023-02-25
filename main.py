from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from summarizer import *
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
    extracted_text = extract_pdf_file(file.file)

    summarized_text = text_summarizer(extracted_text)

    return {"filename": summarized_text}


def extract_pdf_file(file) -> str:
    pdf_reader : PdfReader = PdfReader(file)
    result = ""

    with open('sample.txt', 'w', encoding='utf-8') as f:
        for page_num in range(1, len(pdf_reader.pages)-1):
            page = pdf_reader.pages[page_num]
            result += page.extract_text()
            
        f.write(result)

    return clean_text(result)
    


def clean_text(s: str) -> str:
    # # Remove 'References' at end of paper
    # s = ''.join(s.split('References')[:-1])

    # Remove text within square or round brackets
    s = re.sub(r'[\[\(].*?[\]\)]', '', s)

    # Remove variable spaces between hyphens
    s = re.sub(r'\s*-\s*', '', s)

    # # Remove numbers and numbers with symbols within
    # s = re.sub(r'\b\w*[\d,]+\w*\b', '', s)
    
    # Remove extra white spaces
    s = re.sub(r'\s\s+', ' ', s)

    # Remove newline
    s = s.replace(r'\n', ' ')

    return s
