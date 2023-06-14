"""
The main bot file.
"""

import textwrap
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.callbacks import get_openai_callback
from openai.error import AuthenticationError
from langchain.vectorstores import Chroma


class Bot:
    """
    The bot class.
    """

    def __init__(self):
        self.llm = OpenAI(temperature=0, max_tokens=200, verbose=True)
        self.chain = None

    def ask(self, vectorstore, question):
        """
        Asking the bot a question.
        """

        # Using the LLMChain to make your own prompt.
        prompt = PromptTemplate(template=textwrap.dedent("""
        Provided is the name of a user, followed by a question.
        Write a short, crisp mail, answering the question based on the information provided in the context.
        Make sure to exclude any information that is not relevant to the question.
        Do not hallucinate. If you cant find the answer in the context, mention that you dont know.
        #####

        Context:
        {context}

        Question:
        {question}"""), input_variables=['context', 'question'])

        most_relevant_source = vectorstore.similarity_search(question, k=1)[
            0].metadata['source']

        self.chain = RetrievalQA.from_chain_type(
            llm=self.llm, chain_type='stuff', retriever=vectorstore.as_retriever(search_kwargs={"k": 4, "filter": {'source': most_relevant_source}}),
            chain_type_kwargs={"verbose": True, "prompt": prompt})

        with get_openai_callback() as callback:
            try:
                response = self.chain.run(question)
            except AuthenticationError:
                response = "Invalid API key."
            print(callback)

        return response
