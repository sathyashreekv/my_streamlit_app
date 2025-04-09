from pymongo import MongoClient
from bson import ObjectId
from pymongo import MongoClient
import os

client = MongoClient("mongodb://localhost:27017/pets")
# client =MongoClient("mongodb://host.docker.internal:27017/pets")
db = client["pet_database"]
users_collection = db["users"]
pet_collection = db["pets"]
request_collection = db["requests"]

# for pet in pet_collection.find():
#     old_path = pet.get("image", "")
#     filename = os.path.basename(old_path.replace("\\", "/"))  # handle backslashes
#     new_path = f"images - Copy/{filename}"
    
#     pet_collection.update_one(
#         {"_id": pet["_id"]},
#         {"$set": {"image": new_path}}
#     )

# print("✅ All image paths updated in database.")


# result = pet_collection.update_many(
#     {"status": "available"},
#     {
#         "$set": {"available": True},
#         "$unset": {"status": ""}
#     }
# )

# print(f"✅ Updated {request_collection.modified_count} pets")