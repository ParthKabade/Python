def Summation(Data):
    Sum=0

    for no in Data:
        Sum=Sum+no

    return Sum

def main():
    Marks=[78,90,56,98,77]

    
    Ret=Summation(Marks)
    
    print("-"*50)
    print("Addition is :",Ret)
    print("-"*50)
if __name__ == "__main__":
    main()