#!/usr/bin/env python3
"""Write a Python function that returns the list of school
having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """To list schools with specific topic
    Args:
        mongo_collection: The pymongo collection object.
        topics: list of topics specified
    Return:
        To return a specific school with a specific topic
    """
    results= mongo_collection.find({"topics": topic})
    return list(results)
