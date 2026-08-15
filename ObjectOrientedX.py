
class Arithematic:

    def Addition(self,No1,No2):
        Ans=No1+No2
        return Ans

    def Substration(self,No1,No2):
        Ans=No1-No2
        return Ans
    
Aobj=Arithematic()

Value1=int(input("Enter the 1st number"))
Value2=int(input("Enter the 2nd number"))

#Ret=Addition(Aobj,Value1,Value2)

Ret=Aobj.Addition(Value1,Value2)     
print("Addition is",Ret)

#Ret=Addition(Aobj,Value1,Value2)

Ret=Aobj.Substration(Value1,Value2)    
print("Substration is",Ret)