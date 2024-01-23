#continued after first.py
import random as rd
rand=rd.randint(1,100)
tries=1
while True:
    num=int(input())
    if(num==rand):
        print(f"Correct!!You got it right in {tries} tries.")
        break
    elif num<rand:
        print("Guess higher!!")
    else:
        print("Guess lower XD")
    tries+=1
