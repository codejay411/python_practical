import pickle
class students:
    def __init__(self):
        self.name=raw_input("enter name")
        self.password=raw_input("enter password")
        self.status=1
        print self.name ," are logged in"
    def display(self):
        print self.name,",",len(self.password)*'*',",",self.status
    
    def check(self,name,password):
          try:
            while True:
                a1=pickle.load(filo)
                if (a1.name==name and a1.password==password):
                    print " you are already login"
                else:
                    pass
        
          except EOFError:   
            filo.close()     
print"welcome"
print"1.log in"
choice=input("if you want to log in press 2 :--- ")
if choice==2:
     a=students()
     filo=open("network.det","ab")
     pickle.dump(a,filo)
     a.display()
     filo.close()
else:
     print "you are enter invalid number"
choice1=input("press 2 for continue: ")
if choice1==2:
     name=raw_input("enter user's name: ")
     password=input("enter user's password: ")
     check(name ,password)
else:
     print "you are enter invalid number"
choice2=input("if you want to log  out  enter 1 otherwise press 2")
if choice2==1:
     name=raw_input("enter user's name")
     password=input("enter user's password")
     filo=open("network.det","rb")
     while True:
         status=1
         a=pickle.load(filo)
         if (a.name==name and a.password==password):
             replace(a.status,status)
             a.display()
             print "you are log out"
         else:
             pass
     
         filo.close()







     
