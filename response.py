import streamlit as st
from openai import AuthenticationError
from prompt import InstructionForBot,instruction_for_bot
from PyPDF2 import PdfReader
import easyocr
from docx import Document
from langchain.schema import  SystemMessage
import streamlit as st
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from openai import AuthenticationError
import sys
from langchain.memory import ConversationBufferWindowMemory
from operator import itemgetter
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI
import time
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from dotenv import load_dotenv
load_dotenv()
prompt_templates = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "{instruction_for_bot} {user_details}"),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{question},")], input_variables=["user_details", "instruction_for_bot"])

llm_model = ChatOpenAI(model= "gpt-3.5-turbo",temperature=0.0, streaming=True)
memory = ConversationBufferWindowMemory(
        llm=llm_model, memory_key="history", return_messages=True,k=10)


def TextExtractor(DocumentFile):
    if DocumentFile.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_bytes = DocumentFile.read()
        reader = easyocr.Reader(['en'])
        results = reader.readtext(image_bytes, paragraph=True)
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


def openaiResponse(Report_file,language,llm):
    Report=TextExtractor(Report_file)
    prompt = f'''{InstructionForBot},Report_file: {Report},Language:{language}'''
    try:
        messages = [SystemMessage(content=prompt)]
        response=llm(messages=messages)
        return True
    except AuthenticationError:
        st.warning(
            body='AuthenticationError : Please provide correct api key 🔑' ,icon='🤖')
        return 'AuthenticationError'
    

def chat_response(text_from_pdf, query, OpenAi_Api_Key):
    try:
        
        prompt_templates = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "{instruction_for_bot} {text_from_pdf}"),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{question},")], input_variables=["text_from_pdf", "instruction_for_bot"])
        chain = (
            RunnablePassthrough.assign(
                history=RunnableLambda(
                    memory.load_memory_variables) | itemgetter("history"),
            )
            | prompt_templates
            | llm_model
        )

        output = ""
        for chunk in chain.stream({"question":query, "text_from_pdf": text_from_pdf, "instruction_for_bot": instruction_for_bot}):
            output += chunk.content
            yield chunk.content
            time.sleep(0.05)
        memory.save_context({"inputs": query}, {"output": output})

    except AuthenticationError:
        st.warning(
            body='AuthenticationError : Please provide correct api key 🔑' ,icon='🤖')
        return 'AuthenticationError'




