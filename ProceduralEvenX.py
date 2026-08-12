def CheckEven(No):
    if(No%2==0):
        return True
    else:
        return False



def main():
    Value=int(input("Enter Number :"))

    Ret=CheckEven(Value)

    if(Ret==True):
        print("Given number is Even ")
    else:
        print("Given number is Odd ")

if __name__=="__main__":
    main()