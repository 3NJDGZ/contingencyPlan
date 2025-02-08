import streamlit as st
from pymongo import MongoClient
import pandas as pd

connectionString = "mongodb+srv://dbAdmin:Password1234@contingency.xxt06.mongodb.net/?retryWrites=true&w=majority&appName=contingency"

# Connect to local MongoDB
client = MongoClient(connectionString)

db = client.get_database("chatdb")
messages = db.messages

st.set_page_config(layout="wide", page_title="Chat App")
st.markdown("# Login")
left, right = st.columns(2)
with left:
    st.text_input("Username", key="username")
    st.text_input("Password", key="password")
