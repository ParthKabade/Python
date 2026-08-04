CheckEven=lambda No :(No%2==0)


def main():
    Value=int(input("Enter Number :"))

    Ret=CheckEven(Value)        #Ret=(No%2==0)

    if(Ret==True):
        print("Given number is Even ")
    else:
        print("Given number is Odd ")

if __name__=="__main__":
    main()