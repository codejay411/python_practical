list=[] # empty list
num=input("enter the number in the list:")
print "items for list are:- "
for i in range(0,num,1):
    list.append(raw_input("enter the %d item"%(i+1)))
print "the list is:--"
print list
num2=raw_input("enter the string: ")
if num2 in list:
    print "exist"
else:
    print "not exist
    "
