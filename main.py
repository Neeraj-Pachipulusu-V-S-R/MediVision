import streamlit as st
from response import mains

st.title('**Health Buddy**')
with st.sidebar:
    OpenAPIAI = st.text_input(
        'OpenAI API Key 🔑' ,placeholder='Paste your key(🔑) here',type='password')
    if not OpenAPIAI:
        st.warning(
            body='Kindly enter you API 🔑 in the side bar to chat with us' ,icon='⚠️')
    
def responseExtractor(Report_file,language,OpenAPIAI):
    st.session_state['response']= mains(Report_file,language,OpenAPIAI)
    

if "response" not in st.session_state:
    st.session_state['response'] = ""

if OpenAPIAI:
    Report_file = st.file_uploader('Upload a pdf file',type=['png','jpeg','jpg','doc','docx','pdf'])
    # print(pdfs.name)
    language = st.selectbox('Select Language',['Hindi','English','Hinglish'])
    analizing_button=st.button("Start Analyzation",on_click=responseExtractor,args=[Report_file,language,OpenAPIAI])
    if analizing_button:
        # st.write(st.session_state['response'])
        collected_messages  = ""
        empty_placeholder = st.empty()
        for chunk in st.session_state['response']:
            if chunk is not None and  chunk.choices[0].delta.content is not None:
                chunk_message = chunk.choices[0].delta.content
                # print(chunk_message)
                collected_messages += chunk_message
                empty_placeholder.write(collected_messages)
                