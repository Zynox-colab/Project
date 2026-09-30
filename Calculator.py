import streamlit as st

#Title
st.title("My Calculator")

#Take input
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

#Select operation
operation = st.selectbox(
  "choose an operation",
  ["Addition","Subtraction","Multiplication","Division"]
)

#Calculate
