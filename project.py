import pickle
class students:
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.login=0
    def create(self):
        name=raw_input("enter your name: ")
        password=int(raw_input("enter your password: "))
        nam=name
        pas=password
@staticmethod        
stud=students()
stud.create()

file1=open("school.txt","r+")           #open file         
rec=file1.readlines()
for i in rec:
    record=i.split(',')
    name=record[0]
    password=record[1]
    status=record[2]
    if(stud.name==name and stud.password==password):
        print "user already login"
        logout=input("if you want to logout then press 1 ")
        if logout==1:
            stud.login=0
        else:
            break
    else:
        stud.login=1

pickle.dump(stud,file1)
file1.close()
