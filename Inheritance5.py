class Base:
    def __init__(self):
        print("Enside base constructor")

    def fun(self):
        print("Inside base fun")

class Derived(Base):
    def sun(self):
        print("Inside derived sun")


dobj=Derived()
dobj.fun()
dobj.sun()

