import sys

def main():
    
    
    if(len(sys.argv)==2):
        DirectoryName=sys.argv[1]
        print(f"Directory Name is {DirectoryName}")
    else:
        print("Invalid number of prameter")

if __name__=="__main__":
    main()