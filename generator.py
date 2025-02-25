import google.generativeai as genai
import os
import streamlit as st

# Securely retrieve API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def generate_answer(query, retrieved_chunks):
    context = "\n".join(retrieved_chunks)

    prompt = f"""
    Use the following context to answer the question:
    Context: {context}

    Question: {query}
    Also answer the question in detail. If there is less information to answer the question, you can also search the internet for more information. But when generating the answer, you should also include the source of the information. Also format the output in a manner that the information that is retrieved from the uploaded document is highlighted.
    """

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    query = "What is AI?"
    retrieved_chunks = [
        "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. It includes areas like machine learning, natural language processing, robotics, and more."
    ]

    answer = generate_answer(query, retrieved_chunks)
    print("Answer:\n", answer)
