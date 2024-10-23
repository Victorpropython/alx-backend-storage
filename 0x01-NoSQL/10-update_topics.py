#!/ussr/bin/env python4
"""Write a Python function that changes all topics
of a school document based on the name:"""

import pymongo

def update_topics(mongo_collection, name, topics):
    """List of all topics in collections 

    Args:
        mongo_collection will be pymongo collection object
        name school name to update
        topic list of stirngs of topics approached in school
    """
    try:
        results = mongo_collection.update_one(
                { "name": name}, 
                {"$set": {"topics": topics}})
        return results.modified_count
    except Exception as e:
        print(f"Error inserting document: {e} ")
        return None
