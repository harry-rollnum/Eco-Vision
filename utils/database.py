from pymongo import MongoClient
from datetime import datetime
import os

MONGO_URI = "mongodb+srv://chaosrider870:7i4gVoGuQcpmFpJf@eco-vision.kdjvwub.mongodb.net/?retryWrites=true&w=majority&appName=eco-vision"
client = MongoClient(MONGO_URI)
db = client["eco_vision"]
logs_collection = db["logs"]
feedback_collection = db["feedback"]

def save_log(image_info, predictions):
    logs_collection.insert_one({
        "timestamp": datetime.utcnow(),
        "image_info": image_info,
        "predictions": predictions
    })

def save_feedback(image_info, feedback, correct_label=None):
    feedback_collection.insert_one({
        "timestamp": datetime.utcnow(),
        "image_info": image_info,
        "feedback": feedback,
        "correct_label": correct_label
    })

def get_logs(limit=10):
    return list(logs_collection.find().sort("timestamp", -1).limit(limit))
