import streamlit as st

# Page Configuration
st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Streamlit Calculator")
st.write("Perform basic arithmetic operations.")

# Inputs
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Choose an operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate Button
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")

    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero.")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")