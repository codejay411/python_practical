unit=input("enter unit of electricity : ")
bill=0
if unit<=150:
 bill=(unit*2.40)
 print "bill of electricity is = ",bill
elif unit>150 and unit<=300:
 bill=(150*2.40)+((unit-150)*3.0)
 print "bill of electricity is = ",bill
else:
 bill=(150*2.40)+(150*3)+((unit-300)*3.20)
 print "bill of electricity is = ",bill