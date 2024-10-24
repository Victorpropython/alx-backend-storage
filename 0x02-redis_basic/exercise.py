#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb."""

import redis
import uuid
from typing import callable, Union
from functools import wraps

class Cache:
    """Creating A classfor  the caching and maintenance"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    # Creating a store data base
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    # Gteating a get function 
    def get(self, key: str, fn: Callable None) -> Union[str, bytes, int, float, None]:
        """Retrieves data from Redis and applies conversion function if needed"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value
    
    def get_str(self. key: str) -> str:
        """ Retrives the data as a string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves the data as an int."""
        return self.get(key, int)

    def count_calls(method: callable) -> callable:
        """Decorator tocount how many times a method is called"""
        def wrapper(self, *args, **kwargs):
            """wrapper function to increament the count"""
            #usingthe methodqualified name
            key = method.__qualname__

            # increamenting the countfor the method
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper
