import streamlit as st

st.title("Breast Cancer Risk Assessment System")

st.write("Click below to open the web application")

url = "http://localhost:5173"  # your frontend URL

st.markdown(f"[Open Application]({url})")