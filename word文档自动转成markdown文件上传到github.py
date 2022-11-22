from asyncore import file_dispatcher
from lib2to3.pgen2.grammar import opmap_raw
from platform import platform
import sys
import os
import platform
from unicodedata import name


def OpenFile(filepath: str):
    systemType: str = platform.platform()
    if 'mac' in systemType:
        filepath : str = filepath.replace()
    else:
        filepath:str=filepath.replace()
        os.startfile()

if __name__ == '__main__':
    OpenFile(filepath=r"C:\Users\henae\OneDrive\HeNaerX\Caching\11.docx+")