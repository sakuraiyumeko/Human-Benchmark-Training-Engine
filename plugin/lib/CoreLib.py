import random
import time
import subprocess
import os

random.seed(time.time_ns())


def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def _cycle(count, min, max):
    result = []
    for i in range(count):
        result.append(random.randint(min, max))
    return result


def Random(level=1, count=1):
    if level < 1:
        print("level must greater than 0.")
    else:
        return _cycle(count, 10 ** (level - 1), 10**level - 1)


def ErrorFlash(msg="Invalid input.", delay=0.7, isclear=1):
    print(msg)
    time.sleep(delay)
    if isclear==1: clear()
    else: return 0
