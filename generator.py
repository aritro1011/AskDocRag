import google.generativeai as genai
import os

# Configure the Gemini API
GEMINI_API_KEY = 'AIzaSyCM5vc0aaPmLtvVUeiM9Ib4PdywR1FUx5I'
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

# Function to generate an answer based on the query and retrieved chunks
def generate_answer(query, retrieved_chunks):
    # Combine retrieved chunks as context
    context = "\n".join(retrieved_chunks)

    # Construct the prompt
    prompt = f"""
    Use the following context to answer the question:
    Context: {context}

    Question: {query}
    Also answer the question in detail.If there is less information to answer the question, you can also search the internet for more information. But when generating answer, you should also include the source of the information. Also format the output in a manner that the information that is retrieved from the uploaded document is highlighted.
    """

    # Generate response using Gemini API
    response = model.generate_content(prompt)
    return response.text

# Example usage
if __name__ == "__main__":
    query = "What is AI?"
    retrieved_chunks = [
        "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. It includes areas like machine learning, natural language processing, robotics, and more."
    ]

    answer = generate_answer(query, retrieved_chunks)
    print("Answer:\n", answer)
