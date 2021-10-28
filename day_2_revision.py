# Day 2 Tries

# from random import choice
# from string import ascii_uppercase
# import string
# from timeit import timeit
# from typing import Match
# import time 

# def random_string(length):
#     return ''.join(choice(ascii_uppercase) for i in range(length))

# c_time = time.time()
# strings = [random_string(320) for i in range(10000)]
# matches = [s for s in strings if s.startswith('AA')]
# print(time.time() - c_time)
# print(len(matches))

# c_time = time.time()
# from patricia import trie
# strings_dict = {s:0 for s in strings}
# strings_trie = trie(**strings_dict)

# matches = list(strings_trie.iter('AA'))
# print(time.time() - c_time)
# print(len(matches))



# ---------------------------------------------------------------------------

# Caching and memoization with @lru_cache

# idea behind caching is to store expensive results in a temporary location,
# called cache
# the Python standard library includes a simple in-
# memory cache out of the box in the functools module. The functools.lru_cache
# decorator can be used to easily cache the results of a function

from functools import cache, lru_cache

@lru_cache()     # lru_cache(maxsize=n)  the cache will store value for max size of n
def sum_2(a, b):
    print("***********calculating sum***************")
    return a+b

print(sum_2(10, 20))
print("================after caching sum of 10, 20==============")
print(sum_2(10, 20))
print(sum_2.cache_info())
sum_2.cache_clear()
print(sum_2(10, 20))   # after clearing the cache 

# ---------------------------------------------------------------------------

#  Joblib : library that provides a simple ondisk cache  works same as lru_cache 
#  result will be stored onn disk

# from joblib import Memory
# memory = Memory(cachedir = '/python/cachedir')
# @memory.cache
# def sum_3(a, b):
#     print("  in function sum_2 ")
#     return a+b

# print(sum_3(10, 20))
# print("********** after calling once **********")
# print(sum_3(10, 20))
