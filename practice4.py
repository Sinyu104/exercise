worker={
    'A':(91,20),
    'B':(75,15),
    'C':(60,25)
}
print(worker[1][1])

#exercise1
A=(91, 20)
B=(75,15)
C=(60,25)
D=(75,10)
E=(80,12)
F=(90,25)
G=(45,14)
H=(95,13)
I=(88,2)
if A[0]>90:
    per=8000
elif A[0]<=90 and A[0]>=70:
    per=6000
else:
    per=4000
overtime=A[1]*200
print('A salery = ',per+overtime)
if B[0]>90:
    per=8000
elif B[0]<=90 and B[0]>=70:
    per=6000
else:
    per=4000
overtime=B[1]*200
print('B salery = ',per+overtime)
if C[0]>90:
    per=8000
elif C[0]<=90 and C[0]>=70:
    per=6000
else:
    per=4000
overtime=C[1]*200
print('C salery = ',per+overtime)
##exercise2
if D[0]>90:
    per=8000
elif D[0]<=90 and D[0]>=70:
    per=6000
else:
    per=4000
overtime=D[1]*200
print('D salery = ',per+overtime)
if E[0]>90:
    per=8000
elif E[0]<=90 and E[0]>=70:
    per=6000
else:
    per=4000
overtime=E[1]*200
print('E salery = ',per+overtime)
if F[0]>90:
    per=8000
elif F[0]<=90 and F[0]>=70:
    per=6000
else:
    per=4000
overtime=F[1]*200
print('F salery = ',per+overtime)
##exercise2
if G[0]>90:
    per=8000
elif G[0]<=90 and G[0]>=70:
    per=6000
else:
    per=4000
overtime=G[1]*200
print('G salery = ',per+overtime)
if H[0]>90:
    per=8000
elif H[0]<=90 and H[0]>=70:
    per=6000
else:
    per=4000
overtime=H[1]*200
print('H salery = ',per+overtime)
if I[0]>90:
    per=8000
elif I[0]<=90 and I[0]>=70:
    per=6000
else:
    per=4000
overtime=I[1]*200
print('I salery = ',per+overtime)

##exercise4
def sal (perf, over):
    if perf>90:
        per=8000
    elif perf<=90 and perf>=70:
        per=6000
    else:
        per=4000
    overtime=over*200
    return per+overtime
print('A salery = ',sal(55,14))
print('B salery = ',sal(96,13))
print('C salery = ',sal(85,22))

#Baska
def Baska(n):
   for i in range(1,n+1):
       print('!'*(n-i), end='')
def Basco(m):
    for i in range(m):
        B.append([])
        B[i].append(1)
        for j in range(1,i):
            B[i].append(B[i-1][j-1]+B[i-1][j])
        if(m!=0):
            B[i].append(1)
                
B=[]
Basco(9)
for i in range(9):
    print(" "*(9-i),end="")
    for j in range(0,i+1):
        print(B[i][j],end=" ")
    print()