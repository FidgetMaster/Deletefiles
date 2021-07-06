import os
import shutil
import time
def main():
    deletedFoldercount = 0
    deletedFilescount = 0
    path = "C:/Users/theul/OneDrive/Desktop/python1/file2"
    days = 5
    seconds = time.time()-(days*24*60*60)
    if(os.path.exists(path)):
        for root, folder, files in os.walk(path):
            if(seconds > get_file_or_folder_age(root)):
                remove_folder(root)
                deletedFoldercount = deletedFoldercount + 1
                break
            else:
                for f in folder:
                    folder_path = os.path.join(root,f)
                    if(seconds > get_file_or_folder_age(folder_path)):
                        remove_folder(folder_path)
                        deletedFoldercount = deletedFoldercount + 1
                for f in files:
                    file_path = os.path.join(root,f)
                    if(seconds > get_file_or_folder_age(file_path)):
                        remove_file(file_path)
                        deletedFilescount = deletedFilescount + 1
        else:
            if(seconds >= get_file_or_folder_age(path)):
                remove_file(path)
                deletedFilescount = deletedFilescount + 1
    else:
        print("Path Not Found")
        deletedFilescount = deletedFilescount + 1
    print("Total Folders Deleted: " + str(deletedFoldercount))
    print("Total Files Deleted: " + str(deletedFilescount))
def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path Is Removed Successfully")
    else:
        print("Unable To Delete Path")
def remove_file(path):
    if not os.remove(path):
        print("Path Is Removed Successfully")
    else:
        print("Unable To Delete Path")
def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime
main()