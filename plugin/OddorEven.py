from plugin.lib.CoreLib import Random, ErrorFlash, MenuTemplate, InputManage, clear
import time

# Plugin name
NAME = "Odd or Even"
MENU_OPTIONS = ["5 Rounds", "10 Rounds", "25 Rounds", "50 Rounds", "Custom"]
TIMES = [5, 10, 25, 50]

OoE_menu1 = MenuTemplate(title=NAME, subtitle="Modes", context=MENU_OPTIONS)
OoE_input = InputManage(max_val=6)


# Main feature
def judge(que, ans):
    if (que % 2 == 1 and ans == 1) or (que % 2 == 0 and ans == 2):
        return "Correct"
    else:
        return "Wrong"


def core(op, custom=1):
    while True:
        print("Choose a difficulty(>=1): ", end="")
        OoE_input.max = 100
        level = OoE_input.get_int()
        if level is None:
            continue
        break

    ques = 1

    while True:
        OoE_input.max = 2
        OoE_input.isc = 0
        que = Random(level)[0]
        print("Odd or Even? (Odd=1, Even=0)")
        print(que)
        start = time.perf_counter()
        ans = OoE_input.get_int()
        end = time.perf_counter()
        if ans is None:
            continue
        OoE_input.isc = 1
        times = end - start
        print(judge(que, ans))
        print("duration: ", times)
        print("Press Enter to Countinue", end="")
        input()
        clear()
        if op == 5:
            if ques >= custom:
                break
        else:
            if ques >= TIMES[op - 1]:
                break
        ques += 1
    return 0


def choose():
    OoE_input.max = 6
    choice = OoE_input.get_int()
    if choice is None:
        return False

    if choice == 6:
        return True

    if choice == 5:
        print("How many questions do you want?", end="")
        count = OoE_input.get_int()
        if count is None:
            return False
        core(op=5, custom=count)
        return False

    if choice <= 5:
        core(op=choice)
        return False


def main():
    while True:
        OoE_menu1.menu()
        isB = choose()
        if isB == True:
            break
    return 0


if __name__ == "__main__":
    main()
