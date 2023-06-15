# Description:

A python script that can:
1. Read multiple txt files you provide
2. Answer your question (in the form of a mail) by selecting the most relevant txt file

# Instructions to run:

Create a folder names "docs". Upload your txt files there.

Since the project works using OpenAI, you will have to create an API key here: https://platform.openai.com/account/api-keys

Once you have your key, paste it in the ".env.example" file and rename this file to ".env".

Finally, run:

```bash
pip install -r requirements.txt

python run.py
```

To use the UI to ask questions, run:

```bash
streamlit run app.py
```

You can also run the notebook version: [./demo_notebook](./demo_notebook.ipynb)
