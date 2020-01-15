from math import sqrt
n=int(input("enter the number: "))
count=0
for i in range(2,round(sqrt(n))):
    if n%i == 0:
        print("not prime")
        break
else:
    print("prime")