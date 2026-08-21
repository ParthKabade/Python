def main():
    try:
        fobj=open("Demo.txt","w")
        print("File gets opened")

        fobj.write("Jay Ganesh.............")
#Buffer म्हणजे काय?

#Buffer म्हणजे RAM मधील एक तात्पुरती Memory.

#कारण प्रत्येक Character Disk वर लिहिणे खूप Slow असते.
        fobj.close()

    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()

""""
Program Start
      │
      ▼
main()
      │
      ▼
open("Demo.txt","w")
      │
      ▼
Create/Open File
      │
      ▼
Return File Object
      │
      ▼
write()
      │
      ▼
Data goes to Buffer
      │
      ▼
close()
      │
      ▼
Buffer → Disk
      │
      ▼
Close File
      │
      ▼
Program End
"""

