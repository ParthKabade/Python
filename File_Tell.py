def main():
    try:
        fobj=open("Demo.txt","r")
        print("File gets opened")

        print(f"File offset is :{fobj.tell()}")
        Data=fobj.read(10)
#tell() म्हणजे काय?
#tell() ही File Object ची Method आहे जी सध्याचा File Pointer (File Offset) कुठे आहे ते सांगते.

#* File Open केल्यावर → tell() = 0
#* read(10) नंतर → tell() = 10
#* read(5) आणखी केल्यावर → tell() = 15
        print(Data)
        print(f"File offset is :{fobj.tell()}")
        
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()

"""
Program Start
       │
       ▼
open("Demo.txt","r")
       │
       ▼
Pointer = 0
       │
       ▼
tell()
       │
       ▼
0
       │
       ▼
read(10)
       │
       ▼
Read first 10 characters
       │
       ▼
Pointer = 10
       │
       ▼
tell()
       │
       ▼
10
       │
       ▼
close()
"""