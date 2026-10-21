\# 💬 Sentiment Analysis using LLMs



A text sentiment analysis application built with Python, Streamlit, LangChain, and Groq. The application uses parallel LLM tasks to analyze user-provided text and generate four outputs.



\## Features



\- \*\*Text Analysis:\*\* Explains the meaning of the input text.

\- \*\*Sentiment Classification:\*\* Classifies the text as Positive, Negative, or Neutral.

\- \*\*Follow-up Question:\*\* Generates a relevant question about the text.

\- \*\*Topic Detection:\*\* Identifies the main topic of the text.

\- \*\*Parallel Execution:\*\* Uses LangChain's `RunnableParallel` to execute four LLM chains concurrently.

\- \*\*Interactive Interface:\*\* Provides a simple interface built with Streamlit.



\## Technologies



\- Python

\- Streamlit

\- LangChain

\- LangChain-Groq

\- Groq API

\- `RunnableParallel`



\## Project Structure



```text

sentiment-analysis-llm/

├── app.py

├── .env

├── .gitignore

├── README.md

└── .venv/

```



The `.env` file contains the API key and must never be committed to GitHub. The `.venv/` directory contains the local virtual environment and is also excluded from version control.



\## Prerequisites



\- Python 3.11

\- A Groq account and API key



\## Installation



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd sentiment-analysis-llm

```



\### 2. Create and activate a virtual environment



On Windows:



```bat

py -3.11 -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

python -m pip install --upgrade pip

pip install streamlit langchain-groq langchain-core python-dotenv

```



\### 4. Configure the API key



Create a `.env` file in the project root:



```dotenv

GROQ\_API\_KEY=your\_groq\_api\_key\_here

```



Replace the placeholder with your own Groq API key. Never publish your real API key.



\### 5. Run the application



```bash

streamlit run app.py

```



The application will open in your browser, usually at `http://localhost:8501`.



\## How It Works



The application uses LangChain's `RunnableParallel` to execute four independent chains:



1\. Text analysis

2\. Sentiment classification

3\. Follow-up question generation

4\. Topic detection



Each chain uses the configured chat model through Groq and returns its result to the Streamlit interface.



\## Example



\*\*Input:\*\*



> I really love this application. It is simple, useful, and saves me a lot of time.



\*\*Expected outputs:\*\*



\- \*\*Text Analysis:\*\* The speaker appreciates the application's simplicity and usefulness.

\- \*\*Sentiment:\*\* Positive

\- \*\*Follow-up Question:\*\* What specific features of the application do you find most useful?

\- \*\*Topic:\*\* Application



Actual outputs may vary depending on the model response.



\## Security



\- Never commit `.env` or expose your API key.

\- Keep `.venv/` out of version control.

\- If an API key is accidentally published, revoke it and create a new one.



\## Author



Created as a practical project exploring LLMs, sentiment analysis, and parallel task execution.



