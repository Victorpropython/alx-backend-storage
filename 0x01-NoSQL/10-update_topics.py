#!/usr/bin/env python3

"""Write a Python function that changes all topics
of a school document based on the name:"""

def update_topics(mongo_collection, name, topics):
    """List of all topics in collections 

    Args:
        mongo_collection will be pymongo collection object
        name school name to update
        topic list of stirngs of topics approached in school
    Return:
        None
    """
    mongo_collection.update_many(
            { "name": name},
            {"$set": {"topics": topics}}
        )
