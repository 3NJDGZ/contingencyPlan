# import streamlit
from pymongo import MongoClient
import streamlit

connectionString = "mongodb+srv://dbAdmin:Password1234@contingency.xxt06.mongodb.net/?retryWrites=true&w=majority&appName=contingency"

client = MongoClient(connectionString)

db = client.testDB
usersDB = db.users

# usersDB.insert_one({"name": "John", "age": 30})

for person in usersDB.find():
    print(person)

streamlit.write("Hello World")

# try:
#     client = MongoClient(connectionString)  # Change this if using a different host
#     db = client.test  # Test connection with a sample database
#     print("Connection successful!")
# except Exception as e:
#     print("Connection failed:", e)
