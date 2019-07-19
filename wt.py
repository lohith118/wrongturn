print("enter the numbers within 20")
a=list(map(int,input().split()))
b=[]
for i in range(a):
  if(a.count(i)>=2 and i not in b):
    b.append(i)
print(b)    
