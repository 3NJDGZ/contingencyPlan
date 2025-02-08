import streamlit as st
from pymongo import MongoClient

connectionString = "mongodb+srv://dbAdmin:Password1234@contingency.xxt06.mongodb.net/?retryWrites=true&w=majority&appName=contingency"

# Connect to local MongoDB
client = MongoClient(connectionString)

db = client.get_database("chatdb")
messages = db.messages

st.write("Hello World")
