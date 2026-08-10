
def main():
    Marks=list()
    Size=0

    print("Enter the number of elements :")
    Size=int(input())
    print("Enter the elements :")

    for i in range(Size):
        no=int(input())
        Marks.append(no)


    print(Marks)




if __name__ == "__main__":
    main()