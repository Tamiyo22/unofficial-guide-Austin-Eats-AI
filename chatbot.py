
import streamlit as st
from app import logged_ask_pipeline
from ingest import load_documents
from chunker import split_documents
from store import build_index, index_exists

st.set_page_config(
    page_title="Austin Eats AI",
    page_icon="🍽️",
    layout="centered",
)


@st.cache_resource(show_spinner="Preparing Austin restaurant database...")
def prepare_database():
    corpus = "austin_restaurants"

    if not index_exists(corpus=corpus):
        documents = load_documents(corpus)
        chunks = split_documents(documents)
        build_index(chunks, corpus=corpus)

    return True


try:
    prepare_database()
except Exception as exc:
    st.error(f"Unable to prepare the restaurant database: {exc}")
    st.stop()

st.title("🍽️ Austin Eats AI")
st.caption("Your AI-powered guide to restaurants in Austin, Texas.")


st.info(
    """
    🌮 **Welcome to Austin Eats AI!** 🤠

    Your AI-powered restaurant guide to Austin, Texas!

    **🍽️ What can Austin Eats AI do?**

    Austin Eats AI helps you discover local restaurants using
    a curated Austin restaurant dataset.

    You can:
    - 🔎 Find restaurants by neighborhood
    - 🌮 Explore different cuisines and dining options
    - 💰 Discover restaurants that fit your budget
    - 🍴 Get recommendations based on available restaurant information
    - 🔗 Visit restaurant websites directly from the recommendations

    **🧠 How does it work?**

    Powered by Retrieval-Augmented Generation (RAG), Austin Eats AI
    searches its restaurant database and uses Google Gemini to
    generate answers grounded in the retrieved information.

    If a question falls outside its restaurant knowledge,
    the chatbot is designed to politely decline rather than guess.

    **🌵 Explore Austin:**

    🌮 Central Austin | 🌆 Downtown | 🌶️ East Austin

    🍔 Far North Austin | 🍕 North Austin | 🌯 Northeast Austin

    🥑 Northwest Austin | 🍖 South Austin | 🌵 South Congress

    🍹 South Lamar | 🥩 Southeast Austin | ⭐ West Austin

    **💬 Try asking:**
    "Where can I find affordable restaurants in South Congress?"
    """
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Where should I eat in Austin?")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Finding restaurants..."):
            try:
                outcome = logged_ask_pipeline(
                    question,
                    corpus="austin_restaurants",
                )
                answer = outcome.get(
                    "answer", "Sorry, I couldn't find an answer."
                )
            except Exception:
                answer = (
                    "Something went wrong while searching. "
                    "Please try again."
                )

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
