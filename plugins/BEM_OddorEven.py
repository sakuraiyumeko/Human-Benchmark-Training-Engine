from RandomCore import Random
import time

def judge(que,ans):
    if que%2==ans: return "Correct"
    else: return "Wrong"

def main():
    print("Choose a difficulty(>=1): ",end='')
    level=int(input())
    while True:
        que=Random(level)[0]
        print("Odd or Even? (Odd=1, Even=0)")
        print(que)
        start=time.perf_counter()
        ans=int(input())
        end=time.perf_counter()
        times=end-start
        print(judge(que,ans))
        print("duration: ",times)
        print("Countinue?(Y/N)",end="")
        cont=input()
        if cont=='Y' or cont=='y': continue
        else: break
        
main()