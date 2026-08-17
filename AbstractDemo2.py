from abc import ABC,abstractmethod

class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):
        pass

class Derived(Base):
    def Addition(self,No1,No2):
        return No1+No2
    pass

dobj=Derived()    
Ret=dobj.Addition(11,21)      
print("addition is ", Ret)    