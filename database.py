import pymongo
from pymongo import MongoClient

try:
    uri = "mongodb+srv://dbAdmin:Password1234@contingency.xxt06.mongodb.net/?retryWrites=true&w=majority&appName=contingency"

    client = MongoClient(uri)

    database = client["testDB"]

    collection = database["users"]

    # start example code here

    # end example code here

    client.close()
    print("Connected to mongoDB!")

except Exception as e:
    raise Exception("The following error occurred: ", e)
