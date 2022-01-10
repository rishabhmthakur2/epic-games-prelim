"""
Implement the following requirements using any language or pseudocode: 
● A minimal "User" class containing a unique User ID, User Name, and Email Address.
● One public function/method which accepts as input a list of User IDs and returns a set of 
instances of Users found in an existing database table. Be sure to open the DB connection, 
execute a query, and process the record(s).
"""

# Importing pymongo library to use mongodb online cluster
from pymongo import MongoClient

# Connecting to MongoDB cluster using MongoClient
# Replace username and password with real values
client = MongoClient("mongodb+srv://<username>:<password>@epic-games.xtexu.mongodb.net/?retryWrites=true&w=majority")

# Creacting/Connecting to a database and a collection
db = client["epic-games"]
users = db["users"]

# User class
class User:
    # Constrcutor function that takes in the required params and creates a new User object in the DB
    def __init__(self, userID, userName, userEmail):
        newUser = {
            # Setting userID as MongoDB's unique _id field in order to maintain uniqueness
            "_id": userID,
            "userName": userName,
            "userEmail": userEmail
        }
        # Error handling to return errors while adding to DB
        try:
            users.insert_one(newUser)
            print('New user inserted into the collection')
        except Exception as e:
            print("An exception occurred ::", e)
    # getUsers function to return a set of users based on array of userIds received
    # Will return NONE if userId is not found
    def getUsers(userIDs):
        #Creating an empty list
        userData = list()
        # Looping and searching for each userId
        for userID in userIDs:
            user = users.find_one({"_id": userID})
            userData.append(user)
        return userData
        # Could have also used the $in comparision operator
        # return users.find({"_id": {"$in": userIDs}})

user1 = User("rishabhthakur", "rishabh", "rishabh_thakur@berkeley.edu") # Will give error as already exists
user2 = User("rishabh0504", "rishabhthakur", "rishabhmthakur05@gmail.com") # Should get added as unique id
print(User.getUsers(["rishabhthakur", "1"])) # Will return result for id 1 (exists) and error for id 2 (doesn't exist)