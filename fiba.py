line=input("enter the limit of series")
a=0
b=1
c=0
for i in range(line+1):
    print c,
    a=b
    b=c
    c=a+b
    if (c>line):
        break
