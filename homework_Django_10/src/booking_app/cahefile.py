from time import sleep
from functools import lru_cache
from random import randint
CACHE_DATA = {}


@lru_cache()
def get_data(key_data, *args):
    if key_data in CACHE_DATA:
        CACHE_DATA[key_data] = randint(1, 10)
        return CACHE_DATA[key_data]
    else:
        sleep(5)
        CACHE_DATA[key_data] = 1
        return CACHE_DATA[key_data]


print(CACHE_DATA)

print(get_data(1))
print(get_data(1, 23))
print(get_data(1))
print(get_data(1))
print(get_data(1, 15))

print(CACHE_DATA)
