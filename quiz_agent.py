from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

def generate_quiz(text):

    prompt = f"""
    Generate 5 MCQ questions with answers from this content.

    Content:

    {text[:15000]}
    """

    response = llm.invoke(prompt)

    return response.content