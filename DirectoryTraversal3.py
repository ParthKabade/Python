import os


def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print("Folder name :",FolderName)

        for subf in SubFolder:
            print("Subfolder name is :",subf)

        for fname in FileName:
            print("file name is :",fname)


        
    

if __name__=="__main__":
    main()

"""
Folder name : Marvellous
Subfolder name is : Mumbai
Subfolder name is : Pune
file name is : .DS_Store
Folder name : Marvellous/Mumbai
file name is : File_TellX.py
file name is : File_Remove.py
file name is : File_ReadX.py
file name is : File_Tell.py
file name is : File_Read_Seek.py
file name is : File_Read.py
Folder name : Marvellous/Pune
file name is : ScheduleDemo4.py
file name is : ScheduleDemo1.py
file name is : ScheduleDemo2.py
file name is : ScheduleDemo3.py
"""