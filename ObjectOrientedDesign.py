
class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
        

    def Addition(self):
        Ans=self.No1+self.No2
        return Ans

    def Substration(self):
        Ans=self.No1-self.No2
        return Ans
    


Value1=int(input("Enter the 1st number"))
Value2=int(input("Enter the 2nd number"))

Aobj=Arithematic(Value1,Value2)

#Ret=Addition(Aobj,Value1,Value2)

Ret=Aobj.Addition()     
print("Addition is",Ret)

#Ret=Addition(Aobj,Value1,Value2)

Ret=Aobj.Substration()    
print("Substration is",Ret)