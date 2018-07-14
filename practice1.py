row=5
#star=5
while row!=0:
    star=row
    while star!=0:
        print("*",end="")
        star-=1
    print()
    row-=1



star=5
while star!=0:
    print("*"*star)
    star-=1

row=5
while row!=0:
    star=row
    space=row
    while space!=5:
        print(" ", end="")
        space+=1
    while star!=0:
        print("*",end="")
        star-=1
    print()
    row-=1


