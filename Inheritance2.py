class Base:
    def __init__(self):
        print("Enside base constructor")

class Derived(Base):
    def __init__(self):
        print("inside derived constructor ")


bobj=Base()

