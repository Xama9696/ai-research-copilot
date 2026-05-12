import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from rag.pdf_loader import load_pdf
from rag.rag_chain import ask_question
from agents.summarizer import summarize_text
from agents.quiz_agent import generate_quiz


st.set_page_config(
    page_title="AI Research Copilot",
    layout="wide"
)

st.title("🧠 AI Research Copilot")

uploaded_pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_pdf:

    with st.spinner("Reading PDF..."):

        text = load_pdf(uploaded_pdf)

    st.success("PDF Loaded Successfully!")

    option = st.selectbox(
        "Choose Action",
        [
            "Ask Questions",
            "Generate Summary",
            "Generate Quiz"
        ]
    )

    # -----------------------------
    # ASK QUESTIONS
    # -----------------------------

    if option == "Ask Questions":

        question = st.text_input(
            "Ask Question From PDF"
        )

        if question:

            with st.spinner("Generating Answer..."):

                answer = ask_question(
                    text,
                    question
                )

            st.subheader("Answer")

            st.write(answer)

    # -----------------------------
    # SUMMARY
    # -----------------------------

    elif option == "Generate Summary":

        if st.button("Generate Summary"):

            with st.spinner("Generating Summary..."):

                summary = summarize_text(text)

            st.subheader("Summary")

            st.write(summary)

    # -----------------------------
    # QUIZ
    # -----------------------------

    elif option == "Generate Quiz":

        if st.button("Generate Quiz"):

            with st.spinner("Generating Quiz..."):

                quiz = generate_quiz(text)

            st.subheader("Quiz")

            st.write(quiz)