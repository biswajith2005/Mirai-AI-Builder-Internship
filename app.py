import streamlit as st

st.title("My AI")
st.write("This is a basic UI")

user_message = st.text_input("what is you favourite contry?")

if st.button ("Click this button"):
    st.write(user_message)

print(user_message)