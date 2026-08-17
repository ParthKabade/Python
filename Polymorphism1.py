class Base:
    def fun(self):
        print("Inside base fun")

class Derived(Base):
    def fun(self):
        print("inside drived fun")   

dobj=Derived()
dobj.fun()