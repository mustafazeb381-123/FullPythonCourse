import time
from functools import lru_cache
@lru_cache(maxsize=32)
def some_work(n):
    #some task taking n second
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(4)
    some_work(6)
    print("Done....calling")
    input()
    some_work(3)
    print("calling again")