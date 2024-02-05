import streamlit as st
from response import openaiResponse,TextExtractor,chat_response
from langchain.callbacks import StreamlitCallbackHandler
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
    language = st.selectbox('Select Language',['Hindi','English','Hinglish'])
    if Report_file and language:
        llm = ChatOpenAI(api_key=OpenAPIAI,temperature=0.0,verbose=True,streaming=True,callbacks=[StreamlitCallbackHandler(st.empty())])
        analizing_button=st.button("**Start Analyzation**",on_click=openaiResponse,args=[Report_file,language,llm])

        chat_button= st.checkbox('Do you want to chat with my assistent')
        if "report_text" not in st.session_state:
            st.session_state.report_text = None
        text_from_pdf = TextExtractor(Report_file)
        st.session_state.report_text=text_from_pdf
        if chat_button==True:
                if "messages" not in st.session_state:
                    st.session_state.messages = []
                for message in st.session_state.messages:
                        with st.chat_message(message["role"]):
                            st.markdown(message["content"])
                if prompt := st.chat_input("Ask Query?", key='QueryKeyForTextInput'):
                    # Add user message to chat history
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    # Display user message in the chat message container
                    with st.chat_message("user"):
                        st.markdown(prompt)
                    with st.spinner(text="Thinking..."):
                        # response=chat_response(st.session_state.report_text, prompt, OpenAPIAI)
                        # placeholder = st.empty()
                        # full_response=""
                        full_response=st.write_stream(chat_response(st.session_state.report_text, prompt, OpenAPIAI))
                        # for chunk in response:
                        #     full_response+=chunk
                        #     if bool(chunk):
                        #         # placeholder.markdown(full_response + "")
                        #     print(full_response)
                        st.session_state.messages.append({"role": "assistant", "content": full_response})
                        
                    
