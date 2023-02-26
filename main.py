from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from summarizers import *
import re
#from bert import bert_summarizer
from summarizer.sbert import SBertSummarizer
from extractKeywords import generate_infographic, generate_slides_images
from slideshow import generate_powerpoint
from extractImage import extract_image
from translator import translate

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
    model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
    summarized_text = model(extracted_text, num_sentences=5)
    
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    # Extract Images from pdf file
    extract_image(file.file)
    # Generate infographic
    generate_infographic(extracted_text)
    # Generate slide images
    generate_slides_images(extracted_text)
    # Generate powerpoint
    generate_powerpoint()

    print("done")

    return {"text": summarized_text}


@app.get("api/translate")
def translate(text: str, langauge_from: str, language_to: str):
    try:
        result = translate(text, langauge_from, language_to)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
    return {"text": result}


def extract_pdf_file(file) -> str:
    pdf_reader : PdfReader = PdfReader(file)
    result = ""

    for page_num in range(1, len(pdf_reader.pages)-1):
        page = pdf_reader.pages[page_num]
        result += page.extract_text()
    
    return clean_text(result)
    


def clean_text(s: str) -> str:
    # Remove newline
    s = s.replace('\n', ' ')
    
    # Remove 'References' at end of paper
    temp = s.split('References')
    s = ''.join(temp[:-1]) if len(temp) > 1 else temp[0]

    # Remove Page Numbers
    s = re.sub(r'Page \d+ of \d+ ', '', s)

    # Remove text within square or round brackets
    s = re.sub(r'[\[\(].*?[\]\)]', '', s)

    # Remove variable spaces between hyphens
    s = re.sub(r'\s*-\s*', '', s)

    # # Remove numbers and numbers with symbols within
    # s = re.sub(r'\b\w*[\d,]+\w*\b', '', s)
    
    # Remove extra white spaces
    s = re.sub(r'\s\s+', ' ', s)

    # Remove white spaces in front of punctuations
    s = re.sub(r'\s(?=[\.,;-])', '', s)
    
    return s
