a=int(input())
b=int(input())
if a < b:
    s=a
else:
    s=b    
l=[]
for i in range(1,s+1):
    if (a%i ==0) and (b%i ==0):
        l.append(i)
print(l)
