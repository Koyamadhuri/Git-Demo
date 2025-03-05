num=int(input('enter a number:'))
i=1
c=0
while num>=i:
    if num%i==0:
        c=c+1
    i=i+1
if c==2:
    print("it is a prime:")
else:
    print("it is not a prime")