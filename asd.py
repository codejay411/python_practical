import pickle
class students:
    def _init_(self):
        self.name=" "
        self.password=" "
        self.log=0
    def read(self):
        name=raw_input("enter your name: ")
        password=int(raw_input("enter your password: "))
stud=students()
stud.read()
file1=open("sch.txt","w+")

pickle.dump(stud,file1)
file1.close()
