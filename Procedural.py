def Addition(No1,No2):
    Ans=No1+No2

    return Ans

def Substration(No1,No2):
    Ans=No1-No2

    return Ans

Value1=int(input("Enter the 1st number"))
Value2=int(input("Enter the 2nd number"))

Ret=Addition(Value1,Value2)
print("Addition is",Ret)

Ret=Substration(Value1,Value2)
print("Substration is",Ret)