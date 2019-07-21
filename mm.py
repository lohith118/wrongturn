n=int(input("enter the input size"))
b=[]
a=list(map(int,input().split()))
for i in range(0,n):
    if(a[i]==i):
        b.append(a[i])
if(b!=[]):
    print(b)        
else:
    print(-1)
