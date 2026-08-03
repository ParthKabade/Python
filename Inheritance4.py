class Base:
    def __init__(self):
        print("Enside base constructor")

    def fun(self):
        print("Inside base fun")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("inside derived constructor ")


dobj=Derived()
dobj.fun()

