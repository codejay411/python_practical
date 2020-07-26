print "reverse order of string line by line"
name=raw_input("enter the string:")
line=len(name)
for i in range(-1,-line-1,-1):
    print name[i], 
