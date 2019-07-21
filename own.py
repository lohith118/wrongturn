c=int(input("enter the number"))
print("enter",c,"numbers")
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return (res)
lst=list(map(int,input().split()))
b=(convert(lst))
n=b
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
print(r)
