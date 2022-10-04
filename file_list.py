import glob
import os


def file_list():
    """ This is a red team project, We are preparing a Tool(function) that will accept an input from user which will be a path of a file and
search for certain critial keywords, once it finds out the tool will return to the user in the form of dictionary-->list.
eg :
file_name : -------
keyword_matched : -----
Directory_in : ------
"""

    path = r'D:\CYBER-SECURITY\Hacking_BOOKS'
    # fpath = glob.glob("{0}\**\*".format(path), recursive=True)
    # fpath = glob.glob("{0}\*.bat".format(path), recursive=True):
    # fpath = glob.glob("{0}\**\*.py".format(path), recursive=True):
    # fpath = glob.glob("{0}\**\*.bat".format(path), recursive=True):

    for fpath in glob.glob("{0}\**\*".format(path), recursive=True):
        fsize = os.stat(fpath).st_size/1024
        # print('{0} is {1}', format(fpath, fsize))
        print(fpath, "is", fsize, "KB")


# print(file_list.__doc__)
# print(dir(file_list))


# Second Trial
"""
#from.import iso

#from six import add_metaclass, iteritems
#import iso

import isoparser
iso = isoparser.parse(r'D:\CYBER-SECURITY\Hacking_BOOKS')
keys = iso.record()
# print(iso.record("boot", "grub").children)
# print(iso.record("boot", "grub", "grub.cfg").content)
"""


# Third Trial
"""
import glob
import os
import uuid  # univeral unique identifier

def change_direct():
    path = input("Enter a Path:")
    keyword = input("Enter a Keyword/Phrase to search : ")
    search_folder(path, keyword)
    # except:
    #print("Could not find path. Please try again.")
    # change_direct()


contains = []
id_ = uuid.uuid4()


def search_folder(path, keyword):
    global contains
    dirs = os.listdir(path)
    # for every directory that is listed(which includes files)
    for directory in dirs:
        if directory.endswith(".txt"):
            try:
                file_ = open(path + "/" + directory, "r")
                if keyword in file_.read():
                    contains.append(directory)
                    saveFile = open(
                        r"D:\Programming\ALGOSMIC\red-help>" + keyword + " " + str(id_) + ".txt", "a+")
                    saveFile.write(path + "\\" + directory + "\n")
                    saveFile.close()
            except:
                pass
        elif "." not in directory.split(" "):
            search_folder(path + "/" + directory, keyword)


change_direct()
print(contains)
print("The search results has been saved to the folder defined in the script at line 27.")
input("Press enter to exit...")
"""
