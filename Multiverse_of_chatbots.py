import streamlit as st

st.title("THE MULTIVERSE OF CHATBOTS")
st.set_page_config(
    page_title="Multiverse Chatbot",
    page_icon="🌌",
    layout="centered"
)
st.caption("Choose a personality and start chatting.")

personality=st.selectbox("WHo do you want to talk to?",[
    "Virat Kohli",
    "Cristiano Ronaldo",
    "Tony Stark",
    "Sherlock Holmes",
    "Batman",
    "Naruto Uzumaki",
    "Steve Jobs",
    "A Senior Google Software Engineer"
])

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_message=st.text_input("Say something: ")
if st.button("SEND"):
    if user_message:
        ai_instructions= f"""
You are {personality}.
Stay completely in character.
Reply naturally.
Never mention you are an AI.
User: {user_message}
"""
        with st.spinner("Connecting to the multiverse!...."):
            response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents =ai_instructions
            )

            st.success("Message received!")
            st.write(response.text)

    else:
        st.warning("Please type a message first")

