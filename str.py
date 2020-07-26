str=raw_input("enter the string:")
i=0
for c in str:
    if((c>=a and c<=z) or (c>=A and c<=Z)):
        i=i+1
print "number of words is",i
