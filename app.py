import streamlit as st
from retriever import add_document_to_chroma, retrieve_relevant_chunks
from generator import generate_answer
from utils import extract_text_from_pdf, extract_text_from_docx


st.set_page_config(page_title="AskDoc AI", page_icon="🤖", layout="wide")


st.markdown("""
    <style>
        body { font-family: 'Courier New', monospace; }
        .card {
            background-color: var(--background-color);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.02);
        }
        .theme-toggle {
            display: flex;
            justify-content: flex-end;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)


if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

if st.button("🌙 Toggle Theme" if st.session_state.theme == 'light' else "☀️ Toggle Theme"):
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'


if st.session_state.theme == 'dark':
    st.markdown("""
        <style>
            :root {
                --background-color: #1E1E1E;
                --text-color: #FFFFFF;
            }
            body { background-color: var(--background-color); color: var(--text-color); }
        </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🤖 AskDoc AI</h1>", unsafe_allow_html=True)


col1, col2 = st.columns([1, 2])


with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📄 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_docx(uploaded_file)

        add_document_to_chroma(uploaded_file.name, text)
        st.success(f"{uploaded_file.name} uploaded and processed successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("💬 Ask a Question")
    query = st.text_input("Type your question here")

    if st.button("🚀 Get Answer") and query:
        retrieved_chunks = retrieve_relevant_chunks(query)
        answer = generate_answer(query, retrieved_chunks)

        st.markdown("""
            <div class='card'>
                <h3>🔍 Answer:</h3>
                <p>{}</p>
            </div>
        """.format(answer), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
