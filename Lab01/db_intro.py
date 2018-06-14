from pymongo import MongoClient

mongo_uri = ""

# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

# 4. Create document
new_game = {
    "title" : "LOL",
    "description" : "League of Legends"
}

# 5. Insert document into collection
games.insert_one(new_game)