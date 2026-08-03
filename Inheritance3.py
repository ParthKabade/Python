class Base:
    def __init__(self):
        print("Enside base constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("inside derived constructor ")


bobj=Derived()

