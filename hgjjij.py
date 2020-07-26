num=input("enter the number of line: ")
for i in range(num+1):
    for j in range(1,(num-i)+1,1):
        for k in range(j,1,1):
                print k,
        for l in range(i+1,0,-1):
            print l,
    print
