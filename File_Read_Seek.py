#seek(किती positions पुढे/मागे जायचे,कुठून मोजायचे)
#किती positions पुढे/मागे जायचे:0/1/2
#0 starting
#1 current
#2 end
def main():
    try:
        fobj=open("Demo.txt","r")
        print("File gets opened")

        fobj.seek(10,0)#File च्या सुरुवातीपासून (0) 10 positions पुढे जा.

        Data=fobj.read()

        print(Data)

        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()


"""
Program Start
      │
      ▼
Open File
      │
      ▼
Pointer = 0
      │
      ▼
seek(10,0)
      │
      ▼
Pointer = 10
      │
      ▼
read()
      │
      ▼
Read till End of File
      │
      ▼
Print Data
      │
      ▼
Program End
"""