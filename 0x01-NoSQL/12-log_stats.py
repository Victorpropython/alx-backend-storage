#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

def nginx_log_stats():
    # Connecting to the mongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Accessing the database logs and nginx collection
    db = client.logs
    nginx_collection = db.nginx

    log_count = nginx_collection.count_documents({})

    print(f"{log_count} logs")

    # Defining the HTTP methods to check for
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check = nginx_collection.count_documents({"method": "GET", "path":"/status"})
    print(f"{status_check} status check")

    if __name__ == "__main__":
        main()
