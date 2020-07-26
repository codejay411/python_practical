classxi=dict
()
n=input("enter the number of section in class xi: ")
i=1
while i<=n:
    a=raw_input("enter section: ")
    b=raw_input("enter class teacher: ")
    classxi[a]=b
    i=i+1
print "class","\t","section","\t","teacher name"
for i in classxi:
    print "xi","\t",i,"\t",classxi[i]
