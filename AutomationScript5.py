
import sys

def main():
    
    print("-------------------------------------------------------------------------------")
    print("Marvellous Automation script")
    print("-------------------------------------------------------------------------------")
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the direectory")
            print("for better usage please cheack --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
            print("Please exicute the scrip as")
            print("PYthon Filename.py DirectoryName")
            print("Directory name should be asolute path")
        else:
            DirectoryName=sys.argv[1]
            print(f"Directory Name is {DirectoryName}")
    else:
        print("Invalid number of prameter")
        print("please use --u or--h for more info")

    print("-------------------------------------------------------------------------------")
    print("Thank you for using Marvellous Script")
    print("-------------------------------------------------------------------------------")

if __name__=="__main__":
    main()