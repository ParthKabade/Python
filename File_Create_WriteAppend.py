def main():
    try:
        fobj=open("Demo.txt","a")
        print("File gets opened")
#"a" Mode म्हणजे काय?
#"a" म्हणजे Append Mode.

#यामध्ये:
#* जर File आधीपासून असेल → नवीन Data शेवटी (end) जोडला जातो.
#* जर File नसेल → नवीन File तयार होते.
        fobj.write(" Pune Maharashtra")
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()

"""
Internally ("a" Mode)

Python Program
      │
      ▼
open("Demo.txt", "a")
      │
      ▼
Python Interpreter
      │
      ▼
Operating System
      │
      ▼
File Open होते
      │
      ▼
File Pointer → File च्या शेवटी (End of File)
      │
      ▼
write(" Pune Maharashtra")
      │
      ▼
नवीन Data शेवटी Add होतो
      │
      ▼
close()
      │
      ▼
Buffer Flush → Data Disk वर Save → File Close
"""