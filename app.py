import streamlit as st


def main():
    st.title("Welcome to My Streamlit App")
    st.write("This is a simple app to demonstrate Streamlit functionality.")
    
    if st.button("Click Me"):
        st.write("Button clicked!")
    
    user_input = st.text_input("Enter some text:")
    if user_input:
        st.write(f"You entered: {user_input}")