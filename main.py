# import streamlit

connectionString = "mongodb+srv://dbAdmin:Password1234@contingency.xxt06.mongodb.net/?retryWrites=true&w=majority&appName=contingency"

# streamlit.write("Hello World")
from pymongo import MongoClient

try:
    client = MongoClient(
        connectionString
    )  # Change this if using a different host
    db = client.test  # Test connection with a sample database
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
