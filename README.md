# Medical Report Analysis Application

## Overview

This application is designed to analyze human medical reports, providing responses in layman's terms for easy comprehension by non-medical individuals. It features a chat functionality that enables users to interact with their reports using OpenAI and LangChain. The user interface is built using Streamlit, and OCR (Optical Character Recognition) with PyPDF and EasyOCR is employed to extract information from medical reports.

## Features

- **Medical Report Analysis:**
  - OCR (PyPDF and EasyOCR) extracts information from medical reports.
  - The application processes and interprets the extracted data to provide meaningful insights.

- **Layman's Terms Responses:**
  - Complex medical terminology is translated into easily understandable language for non-medical individuals.
  - Clear and concise explanations of the analysis results are provided.

- **Chat Functionality:**
  - OpenAI is integrated for natural language processing, enabling interactive chat features.
  - Users can engage with their medical reports through a chat interface.

- **User Interaction with Code:**
  - Users can interact with their reports using code for customization or further analysis.
 
- **Supported Report Formats:**
  - Users can upload medical reports in the following formats: PDF, PNG, and JPEG.

- **Streamlit Interface:**
  - The user interface is created using Streamlit, ensuring a user-friendly and easily navigable experience.
  - 
- **OpenAI API Key Input:**
  - Users need to provide their OpenAI API key for utilizing the natural language processing features.
  - Follow the instructions below to input your OpenAI API key.
    -- Follow the steps below to input your OpenAI API key into the application:
        1. Visit the [OpenAI website](https://www.openai.com/) and log in to your account.
        2. Navigate to your account settings or API section to find your API key.
        3. Copy your API key from the OpenAI website.
        -- Note: Keep your API key confidential and avoid sharing it publicly. It is recommended to use environment variables or a secure configuration method to protect sensitive information.




## Getting Started

1. **Installation:**
   - Clone the repository: `git clone https://github.com/AIOnGraph/MediVision.git`
   - Install dependencies: `pip install -r requirements.txt`

2. **Running the Application:**
   - Navigate to the project directory and run: `streamlit run main.py`

3. **Usage:**
   - Open the provided URL in your browser to access the application.
     --https://health-report-analysis.streamlit.app/

## Support and Feedback

If you encounter any issues, have feedback, or suggestions, please open an issue on [GitHub](https://github.com/AIOnGraph/MediVision/issues).


