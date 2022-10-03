"""
This is a red team project, We are preparing a Tool(function) that will accept an input from user which will be a path of a file and
search for certain critial keywords, once it finds out the tool will return to the user in the form of dictionary-->list.
eg :
file_name : -------
keyword_matched : -----
Directory_in : ------
"""

"""
import glob
import os

path = r'D:\CYBER-SECURITY\Hacking_BOOKS'
# fpath = glob.glob("{0}\**\*".format(path), recursive=True)
# fpath = glob.glob("{0}\*.bat".format(path), recursive=True):
# fpath = glob.glob("{0}\**\*.py".format(path), recursive=True):
# fpath = glob.glob("{0}\**\*.bat".format(path), recursive=True):


for fpath in glob.glob("{0}\**\*".format(path), recursive=True):
    fsize = os.stat(fpath).st_size/1024
    # print('{0} is {1}', format(fpath, fsize))
    print(fpath, "is", fsize, "KB")

"""


#from.import iso

#from six import add_metaclass, iteritems
#import iso

import isoparser
iso = isoparser.parse(r'D:\CYBER-SECURITY\Hacking_BOOKS')
keys = iso.record()
# print(iso.record("boot", "grub").children)
# print(iso.record("boot", "grub", "grub.cfg").content)
