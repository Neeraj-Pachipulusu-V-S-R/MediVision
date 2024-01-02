from openai import OpenAI
import streamlit as st
from openai import AuthenticationError
from prompt import InstructionForBot
from PyPDF2 import PdfReader
import easyocr
from docx import Document

model="gpt-3.5-turbo"
def TextExtractor(DocumentFile):
    if DocumentFile.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Convert the image to bytes
        image_bytes = DocumentFile.read()

        # Perform OCR on the image bytes
        reader = easyocr.Reader(['en'])
        results = reader.readtext(image_bytes, paragraph=True)

        # Extract and return text
        extracted_text = ""
        for detection in results:
            text = detection[1]
            extracted_text += text + "\n"
        print(extracted_text)
        return extracted_text
    
    elif DocumentFile.name.lower().endswith(('.pdf')):
        pdf_reader = PdfReader(DocumentFile)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    
    else:
        doc = Document(DocumentFile)
        paragraphs = [paragraph.text for paragraph in doc.paragraphs]
        text = '\n'.join(paragraphs)
        return text

def get_completion(prompt, OpenAPIAI,model):
    try:
        open_ai = OpenAI(api_key=OpenAPIAI)
        messages = [{"role": "user", "content": prompt}]
        response = open_ai.chat.completions.create(
            model=model,
            messages=messages, 
            temperature=0,
            stream=True,
        )
        if response is not None:
            return response
    except AuthenticationError:
        st.warning(
            body='AuthenticationError : Please provide correct api key 🔑' ,icon='🤖')
        return ""

def mains(Report_file,language,OpenAPIAI):
    Report=TextExtractor(Report_file)
    prompt = f'''{InstructionForBot},Report:{Report},Language:{language}'''
    response = get_completion(prompt,OpenAPIAI,model)
    print(response)
    return response
