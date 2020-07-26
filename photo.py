class photo():
    def __init__(self,pno,cat,ex):
        self.pno=0
        self.category=" "
        self.exhibit=" "
        
    def fixexhibit(self,cat):
        if self.category=="antique":
            self.exhibit="zaveri"
        else:
            if self.category=="modern":
                self.exhibit="johnsan"
    def call(self):
        s=self.pno,",",self.category,",",self.exhibit
        print s
asd=photo(3,"antique","zaveri")
asd.call()
