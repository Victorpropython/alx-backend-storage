#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in mongo collection.

    Args:
        mongo_collection: The pymongo collection object.
    Returns:
        A list of documents in the collection.
    """
    try:
        documents = list(mongo_collection.find())
        return documents
    except Exception as e:
        print(f"Error listing documents: {e}")
        return[]
