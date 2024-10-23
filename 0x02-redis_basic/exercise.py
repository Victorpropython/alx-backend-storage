#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb."""

import redis
import uuid
from typing import Union

class Cache:
    """
        Creating A classfor  the caching and maintenance
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    # Creating a store data base
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
