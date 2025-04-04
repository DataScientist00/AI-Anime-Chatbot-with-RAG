import streamlit as st
import os
from Rag import setup_rag_chain , search_duckduckgo
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate



st.set_page_config(page_title="Anime Chatbot", layout="centered")
st.title("🤖 AnimeSensei: Anime Chatbot")
st.caption("Enter a URL, then ask a question.")

st.image("your_image.png")

# Initialize session state variables
if 'retriever' not in st.session_state:
    st.session_state.retriever = None
if 'processed_url' not in st.session_state:
    st.session_state.processed_url = ""

mal_url = st.text_input("Enter Anime URL:", key="mal_url_input")

if mal_url:
    if mal_url != st.session_state.processed_url:
        with st.spinner(f"Analyzing URL... This might take a moment."):
            st.session_state.retriever = setup_rag_chain(mal_url)
            st.session_state.processed_url = mal_url
            if st.session_state.retriever:
                st.success("✅ Ready! Ask a question below.")
            else:
                st.error("❌ Failed to process the URL. Please check the link or try another.")
                st.session_state.processed_url = ""

    if st.session_state.retriever and st.session_state.processed_url == mal_url:
        st.markdown("---")
        question = st.text_input("Ask a question about this anime:", key=f"query_{st.session_state.processed_url}")
        if question:
            with st.spinner("🧠 Thinking..."):
                try:
                    # Retrieve documents from FAISS
                    retrieved_docs = st.session_state.retriever.invoke(question)
                    rag_context = "\n".join([doc.page_content for doc in retrieved_docs])

                    # Fetch DuckDuckGo search results
                    duckduckgo_results = search_duckduckgo(question)

                    # Combine both sources as context
                    final_context = f"RAG Data:\n{rag_context}\n\nWeb Search:\n{duckduckgo_results}"

                    # Setup LLM
                    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=1, api_key=os.getenv("GROQ_API_KEY"))
                    prompt = ChatPromptTemplate.from_template(
                        """
                        Answer the following question based on the provided context.
                        Use both retrieved documents and web search results.
                        Answer in Bullet points only not in paragraph.
                        Always tell source of your answer between [Search , RAG].
                        If the information isn't in the context, say you couldn't find it.

                        Context:
                        {context}

                        Question: {input}

                        Answer:
                        """
                    )

                    # Generate the prompt and invoke LLM with a string
                    formatted_prompt = prompt.format(context=final_context, input=question)

                    # Get LLM response
                    response = llm.invoke(formatted_prompt)  # Pass the formatted string instead of a dict
                    st.markdown("**Answer:**")
                    st.success(response.content)
                except Exception as e:
                    st.error(f"An error occurred while getting the answer: {e}")

elif not mal_url and st.session_state.processed_url:
    st.info("Enter a URL above to analyze a new anime.")
    st.session_state.retriever = None
    st.session_state.processed_url = ""
else:
    st.info("Enter a Anime URL to get started.")

st.markdown("---")
st.caption("Powered by Langchain, Groq, FAISS, DuckDuckGo, Streamlit")