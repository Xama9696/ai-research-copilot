from langchain_groq import ChatGroq

def ask_question(text, question):

    llm = ChatGroq(
        model="llama-3.1-8b-instant"
    )

    prompt = f"""
    Answer the question from the PDF content below.

    PDF Content:
    {text[:15000]}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content
    