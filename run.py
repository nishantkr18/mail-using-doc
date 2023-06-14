"""
This file is used to run the application via command line
"""

import os
from dotenv import load_dotenv
from src.load_data import load_data
from src.process_data import process_data
from src.bot import Bot

if __name__ == '__main__':
    print('Running...')

    # Loading environment variables for OpenAI.
    load_dotenv()
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    docs = load_data()

    vectorstore = process_data(docs)

    bot = Bot(vectorstore = vectorstore)
    
    while True:
        question = input("Enter the question. To exit, type 'exit':")
        if question == 'exit':
            break

        response = bot.ask(question)
        print(response)

    del vectorstore
    print('Done')