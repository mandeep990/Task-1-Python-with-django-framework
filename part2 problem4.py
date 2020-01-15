
n=input().split(" ")
upper=0
lower=0
for i in n:
    for j in i:
        if j.isupper():
            upper+=1
        if j.islower():
            lower+=1
print("The number of uppercase letters are: ",upper)
print("The number of lowercase letters are: ",lower)

