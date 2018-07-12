import random

answer = random.randint(1,100)
print("answer = ", answer)
a=0
while a!=answer:
    a=int(input("Enter a number :"))
    if(a>answer):
        print("Too big")
    elif(a<answer):
        print("Too small")
    else:
        print("Correct")
        break
print("end")

        
