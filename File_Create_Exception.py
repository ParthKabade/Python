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
File आहे ?

YES ─────► Open
 │
 NO
 │
 ▼
Create New File
 │
 ▼
Return File Object
 │
 ▼
print()
 │
 ▼
Program End
"""

def main():
    try:
        open("Demo.txt","w")
        print("File gets opened")
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()

"""
"w"

याचा अर्थ:

* File असेल → ती उघडा आणि तिचा जुना डेटा delete करा.
* File नसेल → नवीन File तयार करा.

समजा Current Directory मध्ये Demo.txt नाही

Python internally असे करतो:

Python

↓

Operating System

↓

Is Demo.txt present?

↓

NO

↓

Create Demo.txt

↓

Open it in Write Mode

↓

Return File Object
"""