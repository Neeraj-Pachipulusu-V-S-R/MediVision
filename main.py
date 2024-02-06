import streamlit as st
from response import openaiResponse,TextExtractor,chat_response
from langchain.callbacks import StreamlitCallbackHandler
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI

st.set_page_config(initial_sidebar_state='collapsed',page_icon='📝',layout='wide')
st.title('**📝Health Buddy**')
subheading = st.subheader('Enter an API key in the sidebar to analyze your report.',divider=True)
with st.sidebar:
    OpenAPIAI = st.text_input(
        '**Enter OpenAI API Key 🔑**' ,placeholder='Paste your key(🔑) here',type='password')
if OpenAPIAI:
    subheading.empty()
    Report_file = st.file_uploader('Upload your report',type=['png','jpeg','jpg','docx','pdf'])
    language = st.selectbox('Select Language',['English','Hindi','Hinglish'])
    if Report_file and language:
        if "report_text" not in st.session_state:
               st.session_state.report_text = None
        st.session_state.report_text = TextExtractor(Report_file)
        llm = ChatOpenAI(api_key=OpenAPIAI,temperature=0.0,verbose=True,streaming=True,callbacks=[StreamlitCallbackHandler(st.empty())])
        analizing_button=st.button("**Start Analyzation**",on_click=openaiResponse,args=[Report_file,language,llm])
        Chat_checkbox= st.checkbox('Do you want to chat with my assistent')
        if Chat_checkbox==True:
                if "messages" not in st.session_state:
                    st.session_state.messages = []
                for message in st.session_state.messages:
                        with st.chat_message(message["role"]):
                            st.markdown(message["content"])
                if prompt := st.chat_input("Ask Query?", key='QueryKeyForTextInput'):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    with st.chat_message("user",avatar='userAvtar.png'):
                        st.markdown(prompt)
                    with st.chat_message("assistant",avatar='Assistent.png'):                        
                        full_response=st.write_stream(chat_response(st.session_state.report_text, prompt, OpenAPIAI))
                        st.session_state.messages.append({"role": "assistant", "content": full_response})

               