import streamlit as st
import google.generativeai as genai
st.title("My title")
genai.configure(api_key="AIzaSyBaPZ-p3WH7Lrli-QkDe7LXHJOR8yY-8pQ")
text = input()

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("click me"):
    response = chat.send_message(text)
    st.write(response.text)
