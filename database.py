import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://shk123:22i264@cluster0.fvpzn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["BlockchainDB"]
users_collection = db["Users"]
blocks_collection = db["Blockchain"]

def store_user_keys(user, public_key, private_key):
    """Store user keys in the database"""
    users_collection.insert_one({
        "user": user,
        "public_key": public_key.save_pkcs1().decode(),
        "private_key": private_key.save_pkcs1().decode()
    })

def store_block(block):
    """Store blockchain block in the database"""
    blocks_collection.insert_one(block)
