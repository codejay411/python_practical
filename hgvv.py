class bankaccount:
    def __init__(self,name,openbal):
        self.acholder=name
        self.balance=openbal
        print "bank account created for",self.acholder
    def prn(self):
        print "account holder:",self.acholder
        print "balance: ",self.balance
    def __del__(self):
        print "bank account destroyed for :",self.acholder
ac2003=bankaccount("mr k",6500)
l=ac2003
s=ac2003
ac22=bankaccount("mrs k",2000)
l1=ac22
del l
del l1

