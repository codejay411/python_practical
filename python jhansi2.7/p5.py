num=input("\n\nenter the last number:")
a=0
b=1
c=0
for i in range(1,num+1,1):
 print c,",",
 a=b
 b=c
 c=a+b
 if (c>num):
  break

