d=input("enter ")
y=(d/365)
m=(d%365)/30
w=((d%365)%30)/7
da=(((d%365)%30)%7)
print y,"yet",m,"months",w,"wee",da,"day"
