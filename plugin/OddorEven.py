from plugin.lib.CoreLib import Random, ErrorFlash,MenuTemplate
import time

#Plugin name
NAME = "Odd or Even"

#Main feature
def judge(que, ans):
    if que % 2 == ans:
        return "Correct"
    else:
        return "Wrong"


def core():
    while True:
        print("Choose a difficulty(>=1): ", end="")
        try:
            temp_1_input=int(input())
            if temp_1_input<1:
                ErrorFlash("level must greater than 0.")
                continue
            else:
                level = temp_1_input
            break
        except ValueError:
            ErrorFlash()
            continue

    while True:
        que = Random(level)[0]
        print("Odd or Even? (Odd=1, Even=0)")
        print(que)
        start = time.perf_counter()

        try:
            ans = int(input())
        except ValueError:
            ErrorFlash(isclear=0)
            continue

        end = time.perf_counter()
        times = end - start
        print(judge(que, ans))
        print("duration: ", times)
        print("Countinue?(Y/N)", end="")
        cont = input()
        if cont == "Y" or cont == "y":
            continue
        else:
            break
    return 0

def main():
    return 0

if __name__ == "__main__":
    main()
