"""
Streamlit main app file.
"""

import os
from dotenv import load_dotenv
import streamlit as st
from src.load_data import load_data
from src.process_data import process_data
from src.bot import Bot

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


   
def main():
    """
    Main function.
    """

    if st.session_state.get('bot') is None:
        with st.spinner('Reading and parsing document data...'):
            docs = load_data()
            st.session_state['vectorstore'] = process_data(docs)
            st.session_state['bot'] = Bot()
        st.experimental_rerun()
    else:
        # Asking for question.
        question = st.text_input('Enter your question:', key='question')

        if question:
            with st.spinner("Thinking..."):
                response = st.session_state['bot'].ask(vectorstore=st.session_state['vectorstore'], 
                                                         question=question)
                # Printing relevant documents.
                st.write(response)

if __name__ == '__main__':
    main()
