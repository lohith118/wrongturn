a=int(input("enter the range:"))
print("enter",a,"numbers")
c=list(map(int,input().split()))
b=[]
for i in c:
    if((c.count(c[i]))>1 and i not in b):
        b.append(c[i])
print(len(b))
