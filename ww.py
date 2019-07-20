c=print("enter the range within 20")
print("enter",c,"numbers")
a=list(map(int,input().split()))
b=[]
for i in range(a):
  if(a.count(i)==1 and i not in b):
    b.append(i)
print(b)    
