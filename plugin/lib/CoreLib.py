import random
import time
import subprocess
import os

random.seed(time.time_ns())


class MenuTemplate:
    def __init__(self, title="TITLE", subtitle="SUBTITLE", context=[]):
        self.name1 = title
        self.name2 = subtitle
        self.list = context

    def _check_legality(self):
        if isinstance(self.list, list):
            return True
        else:
            return False

    def menu(self):
        i = 1
        clear()
        if self._check_legality() == True:
            print("-" * 50)
            print("*", self.name1.center(48, " "), "*", sep="")
            print("-" * 50)
            print(self.name2)
            print()

            for l in self.list:
                print(i, ". ", l, sep="")
                i += 1

            print(i, ". ", "quit", sep="")
            print()
            print("Choose an option: ", end="",flush=True)
        else:
            raise TypeError("Error(CoreLib.MenuTemplate): Invalid menu context type")


class InputManage:
    def __init__(self, min_val=1, max_val=4):
        self.min = min_val
        self.max = max_val

    def get_int(self):
        while True:
            try:
                value = int(input())
                if self.min > value or self.max < value:
                    print("Invalid input.")
                    return None
                else:
                    return value
            except (ValueError, TypeError):
                ErrorFlash()
                return None


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
    if isclear == 1:
        clear()
    else:
        return 0
