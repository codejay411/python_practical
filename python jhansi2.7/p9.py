a=input("\nenter the year in 4 digit:")
if a>=1000 and a<=9999:
 if a%4==0:
  print a,"is a leap year"
 else:
  print a,"is not a leap year"
else:
 print a,"is not proper year"