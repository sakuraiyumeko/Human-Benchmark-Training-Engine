import random
import time
import subprocess
import os

random.seed(time.time_ns())


def cycle(count, min, max):
    result = []
    for i in range(count):
        result.append(random.randint(min, max))
    return result


def Random(level=1, count=1):
    assert level >= 1, "level must greater than 0."
    return cycle(count, 10 ** (level - 1), 10**level - 1)


def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
