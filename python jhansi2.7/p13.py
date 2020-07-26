s=raw_input("enter the string:")
i=-1
for c in s:
 if c!=s[i]:
  print ("not pallindrome")
 i=i-1
else:
 print ("pallindrome")
