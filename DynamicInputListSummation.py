
def Summation(Data):
    Sum=0
    for Cnt in Data:
        Sum=Sum+Cnt
    return Sum


def main():
    Marks=list()
    Size=0

    print("Enter the number of elements :")
    Size=int(input())
    print("Enter the elements :")

    for i in range(Size):
        no=int(input())
        Marks.append(no)

    Ret=Summation(Marks)

    print("Summation is",Ret)




if __name__ == "__main__":
    main()