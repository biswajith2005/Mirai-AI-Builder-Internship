import streamlit as st

st.title("THE MULTIVERSE OF CHATBOTS")

#sidebar
personality=st.sidebar.selectbox("WHo do you want to talk to?",[
    "virat kohli","Gratest lover of PC games in the world","A crazy Ronaldo fan"
])

intensity=st.sidebar.slider("Some Name",min_value=1,max_value=10,value=5)

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_message=st.text_input("Say something: ")
if st.button("SEND"):
    if user_message:
        ai_instructions=f"You are acting as {personality} with an intensity level of {intensity}.Respond to the message sent by the user completly in charecter:{user_message}"
        with st.spinner("Connecting to the multiverse!...."):
            response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents =ai_instructions
            )

            st.success("Message received!")
            st.write(response.text)

    else:
        st.warning("Please type a message first")

