import os

def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print("Folder name :",FolderName)

        for subf in SubFolder:
            print("Subfolder name is :",subf)

        
    

if __name__=="__main__":
    main()