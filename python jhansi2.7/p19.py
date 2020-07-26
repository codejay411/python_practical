d=input("enter the number of days : ")
y=(d/365)
m=(d%365)/30
w=((d%365)%30)/7
da=(((d%365)%30)%7)
print y,"year",m,"months",w,"week",da,"day"
