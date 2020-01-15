
#5
def sortdict1(dict1):
    l1=[]
    for i in dict1.keys():
        l1.append(i)
    l1.sort()
    d={}
    for k in range(n):
        d[l1[k]]=dict1[l1[k]]
    return d


def sumlengthkeys(dict1):
    l2=[]
    for i in dict1.values():
        l2.append(i)
    sumvalue=0
    for i in l2:
        sumvalue+=len(i)
    return sumvalue


def reversevalues(dict1):
    l2=[]
    for i in dict1.values():
        l2.append(i)
    l1=[]
    for i in dict1.keys():
        l1.append(i)
    l3=[]
    for k in l2:
        rev=""
        for i in k:
            rev=i+rev
        l3.append(rev)
    for k in range(n):
        dict1[l1[k]]=l3[k]
    return dict1


n=int(input("enter the number of items: "))
dict1={}
for i in range(n):
    a=input("enter the item separated by ':' : ").split(":")
    dict1[a[0]]=a[1]
print(sortdict1(dict1))
print(sumlengthkeys(dict1))
print(reversevalues(dict1))