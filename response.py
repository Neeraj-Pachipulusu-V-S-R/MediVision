import streamlit as st
from openai import AuthenticationError
from prompt import InstructionForBot
from PyPDF2 import PdfReader
import easyocr
from docx import Document
from langchain.schema import  SystemMessage


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


def openaiResponse(Report_file,language,chat):
    Report=TextExtractor(Report_file)
    prompt = f'''{InstructionForBot},Report_file: {Report},Language:{language}'''
    try:
        messages = [SystemMessage(content=prompt)]
        response=chat(messages=messages)
        return True
    except AuthenticationError:
        st.warning(
            body='AuthenticationError : Please provide correct api key 🔑' ,icon='🤖')
        return 'AuthenticationError'

    

