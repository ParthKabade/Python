def main():
    try:
        fobj=open("Demo.txt","w")
        print("File gets opened")

        fobj.write("Marvellous infosystems")
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()

"""
Program Start
      │
      ▼
main()
      │
      ▼
try
      │
      ▼
open("Demo.txt","w")
      │
      ▼
Python Interpreter
      │
      ▼
Operating System
      │
      ▼
Create/Open File
      │
      ▼
File Descriptor = 3
      │
      ▼
Python File Object (fobj)
      │
      ▼
print()
      │
      ▼
stdout (FD = 1)
      │
      ▼
write()
      │
      ▼
Buffer
      │
      ▼
Disk
      │
      ▼
close()
      │
      ▼
Flush Buffer
      │
      ▼
Release FD
      │
      ▼
Program Ends
"""