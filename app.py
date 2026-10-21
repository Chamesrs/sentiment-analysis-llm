
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

st.set_page_config(
    page_title="Sentiment Analysis using LLMs",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Sentiment Analysis using LLMs")
st.write("Analyze text using parallel LLM tasks.")

# Initialize the chat model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

parser = StrOutputParser()

# Task 1: Text analysis
text_prompt = ChatPromptTemplate.from_template(
    "Explain the meaning of this text in 2 short sentences:\n{text}"
)

# Task 2: Sentiment classification
sentiment_prompt = ChatPromptTemplate.from_template(
    "Classify the sentiment of this text as exactly one of: "
    "Positive, Negative, Neutral. Return only the label.\n{text}"
)

# Task 3: Follow-up question
question_prompt = ChatPromptTemplate.from_template(
    "Generate one relevant follow-up question about this text. "
    "Return only the question.\n{text}"
)

# Task 4: Topic classification
topic_prompt = ChatPromptTemplate.from_template(
    "Identify the main topic of this text in 1 to 4 words. "
    "Return only the topic.\n{text}"
)

# Build one chain per task
text_chain = text_prompt | llm | parser
sentiment_chain = sentiment_prompt | llm | parser
question_chain = question_prompt | llm | parser
topic_chain = topic_prompt | llm | parser

# Execute the four chains in parallel
parallel_chain = RunnableParallel(
    text=text_chain,
    sentiment=sentiment_chain,
    follow_up_question=question_chain,
    topic=topic_chain
)

user_text = st.text_area(
    "Enter your text",
    placeholder="Example: I love this application because it saves time.",
    height=150
)

if st.button("Analyze Text", type="primary"):
    if not user_text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            with st.spinner("Running parallel LLM tasks..."):
                result = parallel_chain.invoke({"text": user_text})

            st.success("Analysis completed!")

            st.subheader("📝 Text Analysis")
            st.write(result["text"])

            st.subheader("🎭 Sentiment")
            sentiment = result["sentiment"].strip()
            if sentiment.lower().startswith("positive"):
                st.success(sentiment)
            elif sentiment.lower().startswith("negative"):
                st.error(sentiment)
            else:
                st.info(sentiment)

            st.subheader("❓ Follow-up Question")
            st.write(result["follow_up_question"])

            st.subheader("🏷️ Topic")
            st.write(result["topic"])

        except Exception as e:
            st.error(f"Analysis failed: {e}")
