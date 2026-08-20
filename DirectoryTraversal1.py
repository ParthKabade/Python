import os


def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print(FolderName)

#os.walk() एखाद्या directory मधील सर्व folders आणि files recursively फिरून (traverse करून) माहिती देतो.


if __name__=="__main__":
    main()

"""
Internally काय होतं?

जेव्हा Python ही line execute करतो:

os.walk("Marvellous")

तेव्हा os.walk() एक generator object तयार करतो.

Generator Object म्हणजे अशी वस्तू (Object) जी सर्व डेटा एकाच वेळी मेमरीमध्ये साठवत नाही, तर गरज पडेल तेव्हाच एक-एक value तयार करून देते.

तो लगेच सर्व directories scan करत नाही.

तो म्हणतो:

“जेव्हा for loop मला पुढचा item मागेल, तेव्हा मी एक directory scan करून देईन.”

म्हणून तो memory efficient असतो.

प्रत्येक iteration ला os.walk() tuple return करतो.

उदाहरण:
(
    "Marvellous",
    ["Folder1", "Folder2"],
    ["Demo.py", "Test.txt"]
)

Python internally हे unpack करतो:

FolderName = "Marvellous"

SubFolder = ["Folder1", "Folder2"]

FileName = ["Demo.py", "Test.txt"]



जर तिन्ही print केले तर

Output

Folder : Marvellous
SubFolders : ['Folder1', 'Folder2']
Files : ['Demo.py', 'Test.txt']
----------------------
Folder : Marvellous/Folder1
SubFolders : []
Files : ['A.py', 'B.txt']
----------------------
Folder : Marvellous/Folder2
SubFolders : ['Folder3']
Files : ['C.py']
----------------------
Folder : Marvellous/Folder2/Folder3
SubFolders : []
Files : ['D.py']
----------------------
"""