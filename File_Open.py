def main():
    open("Demo.txt","r")
    print("File gets opened")

if __name__=="__main__":
    main()

    """
Program Start
       │
       ▼
Python Interpreter
       │
       ▼
Create main()
       │
       ▼
__name__ == "__main__"
       │
       ▼
Call main()
       │
       ▼
open("Demo.txt","r")
       │
       ▼
OS ला Request
       │
       ▼
File Descriptor मिळतो
       │
       ▼
TextIOWrapper Object तयार होतो
       │
       ▼
Reference नसल्यामुळे Object नंतर Garbage Collector काढून टाकतो
       │
       ▼
print()
       │
       ▼
Program End
     """