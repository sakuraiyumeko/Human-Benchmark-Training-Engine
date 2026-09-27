import random
import time

random.seed(time.time_ns())


def cycle(count, min, max):
    result = []
    for i in range(count):
        result.append(random.randint(min, max))
    return result


def Random(level=1, count=1):
    return cycle(count,10**(level-1),10**level-1)
