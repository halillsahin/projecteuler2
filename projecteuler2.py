a=[1,2,3,5,8]
n=5
c=0
while True:
    b=a[n-1]+a[n-2]
    a.append(b)
    n+=1
    if b>4000000:
        break
for i in a :
    if i%2==0:
        c+=i
print(c)        

