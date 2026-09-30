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
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

  # Display result
    if result is not None:
        st.success(f"Result: {result}")
