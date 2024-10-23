#!/usr/bin/env python3
import pymongo

"""Write a Python function that inserts a new document
in a collection based on kwargs"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a MongoDB collection based on
    Keyword

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: keyword orguments representing the document fields and 
    Returns:
        the _id of the newly inserted document.
    """
    try:
        results = mongo_collection.insert_one(kwargs)
        return result.inserted_id
    except Exception as e:
        print(f"Error inserting document: {e}")
        return None
