a=int(input("enter the number"))
j=0
b=[]
while(a>0):
    d=a%10
    a=a//10
    if(d<10):
         b.append(d)
r=sorted(b)
vk=t=0
for i in range(0,len(r)-1):
  f=r[i]
  if int(f)!=0:
    for i in range(i+1,i+2):
      f=f+r[i]
      if int(f)<27 and int(f)>0:
         vk=vk+1
      elif int(f)==0:
         vk=vk-1
      else:
         break
if vk!=1:
   j=vk%2
print(vk+j+1)
