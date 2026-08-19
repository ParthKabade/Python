def main():
    try:
        fobj=open("Demo.txt","r")
        print("File gets opened")

        print(f"File offset is :{fobj.tell()}")         #0
        Data=fobj.read(10)                              #Marvellous

        print(Data)
        print(f"File offset is :{fobj.tell()}")         #10
        

        Data=fobj.read(10)                             

        print(Data)                                     # infosyste
        print(f"File offset is :{fobj.tell()}")         #20
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()