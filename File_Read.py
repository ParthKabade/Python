def main():
    try:
        fobj=open("Demo.txt","r")
        print("File gets opened")

        Data=fobj.read(10)
#read(10) मध्ये 10 चा अर्थ

#read(10) म्हणजे 10 bytes नव्हे, तर Python text mode मध्ये साधारणपणे 10 characters वाचण्याचा प्रयत्न करते. जर File मध्ये 10 पेक्षा कमी characters शिल्लक असतील, तर जितके उपलब्ध आहेत तितकेच वाचले जातात.
        print(Data)
        
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

if __name__=="__main__":
    main()

"""
तुमचा Program योग्य आहे. आता हा internally कसा काम करतो ते मराठीत समजून घेऊ.

⸻

Code

def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets opened")
        Data = fobj.read(10)
        print(Data)
        fobj.close()
    except FileNotFoundError:
        print("File is not present in current directory")
if __name__ == "__main__":
    main()

⸻

Step 1 : Program सुरू होतो

जेव्हा तुम्ही

python3 Demo.py

चालवता,

* Python Interpreter सुरू होतो.
* main() function call होते.

⸻

Step 2 : open("Demo.txt", "r")

fobj = open("Demo.txt", "r")

Python Operating System ला सांगते:

“Demo.txt ही file Read Mode मध्ये उघडा.”

OS काय करते?

* File अस्तित्वात आहे का ते तपासते.
* असेल तर ती Open करते.
* नसेल तर FileNotFoundError देते.

समजा File आहे.

OS File Descriptor देते.

उदा.

Demo.txt
↓
File Descriptor = 3

Python त्या FD वरून File Object तयार करते.

fobj
  │
  ▼
Python File Object
    │
    ├── File Name = Demo.txt
    ├── Mode = r
    ├── File Descriptor = 3
    └── File Pointer = 0

⸻

Step 3 : Print

print("File gets opened")

हा Output

stdout (FD = 1)

मार्फत Screen वर दिसतो.

⸻

Step 4 : read(10)

Data = fobj.read(10)

ही सर्वात महत्त्वाची ओळ आहे.

Python म्हणते:

“File मधून 10 characters वाचा.”

⸻

समजा File मध्ये आहे

Marvellous Infosystems

Character Position

M a r v e l l o u s   I n f o s y s t e m s
0 1 2 3 4 5 6 7 8 9 10...

सुरुवातीला

Pointer
↓
Marvellous Infosystems
↑
0

⸻

Python OS ला Request करते

FD = 3
↓
Read 10 characters

OS Disk मधून Data आणते.

Python

हा Data

Data

मध्ये ठेवते.

Data
↓
"Marvellous"

⸻

File Pointer पुढे जातो

आता Pointer

Marvellous Infosystems
          ↑
          10

म्हणजे पुढचा read() इथून सुरू होईल.

⸻

Step 5 : Print Data

print(Data)

Output

Marvellous

⸻

जर पुन्हा

print(fobj.read(5))

केले तर

Pointer आधीच 10 वर आहे.

म्हणून

 Infos

वाचले जाईल.

⸻

जर

print(fobj.read())

केले

तर

बाकीचा पूर्ण Data मिळेल.

⸻

जर

print(fobj.read())
print(fobj.read())

केले

पहिल्या वेळेस

पूर्ण File वाचली जाईल.

दुसऱ्या वेळेस

''

रिकामी String मिळेल.

कारण Pointer File च्या शेवटी पोहोचला आहे.

⸻

Step 6 : Close

fobj.close()

Python

OS ला सांगते

FD = 3
↓
Close

OS

* Buffer साफ करते (जर गरज असेल तर)
* File Descriptor Release करते
* File बंद करते.

⸻

Internal Flow

Program Start
      │
      ▼
main()
      │
      ▼
open("Demo.txt","r")
      │
      ▼
Operating System
      │
      ▼
File Open
      │
      ▼
File Descriptor = 3
      │
      ▼
File Object तयार
      │
      ▼
read(10)
      │
      ▼
Disk
      │
      ▼
10 Characters Memory मध्ये
      │
      ▼
Data Variable
      │
      ▼
print(Data)
      │
      ▼
stdout
      │
      ▼
Screen
      │
      ▼
close()
      │
      ▼
FD Release
      │
      ▼
Program End

read(10) मध्ये 10 चा अर्थ

read(10) म्हणजे 10 bytes नव्हे, तर Python text mode मध्ये साधारणपणे 10 characters वाचण्याचा प्रयत्न करते. जर File मध्ये 10 पेक्षा कमी characters शिल्लक असतील, तर जितके उपलब्ध आहेत तितकेच वाचले जातात.

उदाहरण:

Demo.txt
----------
Marvellous Infosystems
fobj.read(10)

Output:

Marvellous

आणि File Pointer Marvellous नंतरच्या जागेवर जाऊन थांबतो. पुढील read() तिथूनच वाचन सुरू करतो.
"""