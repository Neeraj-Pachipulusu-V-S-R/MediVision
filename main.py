import streamlit as st
from response import openaiResponse
import base64
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI

st.set_page_config(initial_sidebar_state='collapsed',page_icon='📝')

st.title('**📝Health Buddy**')
subheading = st.subheader('Enter an API key in the sidebar to analyze your report.',divider=True)
st.markdown("""
<style>
     [data-testid=StyledLinkIconContainer]{
            color: white;
            font-weight: bold;
            font-family: 'Arial';
    }    
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
     [data-testid=stMarkdownContainer]{
            color: white;
            font-weight: bold;
            font-family: 'Times New Roman';
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
     [data-testid=stApp]{
            color: white;
            font-weight: bold;
            font-family: 'Times New Roman';
    }   
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
     [data-testid=stVerticalBlock]{
            color: white;
            font-weight: bold;
            font-family: 'Times New Roman';
    }   
</style>
""", unsafe_allow_html=True)
# To set the background Image
side_bg_ext = 'png'
side_bg = 'BGIMAGE.png'
st.markdown(
f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: scroll;
}}
</style>
""",
unsafe_allow_html=True,
)

side_bg_ext = 'png'
side_bg = 'sidebar.png'
st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
    }}
    </style>
    """,
    unsafe_allow_html=True,
    )

with st.sidebar:
    OpenAPIAI = st.text_input(
        ':white[**Enter OpenAI API Key 🔑**]' ,placeholder='Paste your key(🔑) here',type='password')
    
if OpenAPIAI:
    subheading.empty()


if OpenAPIAI:
    Report_file = st.file_uploader('Upload your report',type=['png','jpeg','jpg','docx','pdf'])
    language = st.selectbox('Select Language',['Hindi','English','Hinglish'])
    if Report_file and language:
        chat = ChatOpenAI(api_key=OpenAPIAI,temperature=0.0,verbose=True,streaming=True,callbacks=[StreamlitCallbackHandler(st.empty())])
        analizing_button=st.button(":red[Start Analyzation]",on_click=openaiResponse,args=[Report_file,language,chat])
            
                

        

            
