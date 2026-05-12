from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

def summarize_text(text):

    prompt = f"""
    Create concise study notes from this content.

    Content:

    {text[:15000]}
    """

    response = llm.invoke(prompt)

    return response.content