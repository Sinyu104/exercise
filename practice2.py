n=int(input("Enter an integeer :"))
for i in range(2, n+1):
    x=True
    for j in range(2,i):
        if i%j==0  :
            x=False
            break
    if x:
        print(i, 'is prime')
    