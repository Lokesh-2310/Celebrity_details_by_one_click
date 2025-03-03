import streamlit as st
from app import output_response
import time, os

groq_api_key=os.getenv('GROQ_API_KEY')

st.header("Get details of your favourite celebrities :sunglasses:")

user_input = st.text_input("Enter the name of celebrity","VK Kohli")

btn=st.button("Prcoess")


if btn:
    with st.spinner("Gathering information..."):
        response=output_response(groq_api_key=groq_api_key,user_input=user_input)
    
    st.json(response)
            