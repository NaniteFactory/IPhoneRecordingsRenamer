from tkinter import filedialog
from tkinter import *
import os

from xml.etree.ElementTree import *

ASSET_MANIFEST_PLIST = "AssetManifest.plist"
FILE_EXTENSION = ".m4a"

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    pathDir = filedialog.askdirectory()
    pathFilePlist = os.path.join(pathDir, ASSET_MANIFEST_PLIST)
    try:
        tree = parse(pathFilePlist)  # gets an ElementTree object
    except FileNotFoundError as e:
        print(e)
        print("Exit by error above.")
        exit()
    root = tree.getroot()  # gets an Element object

    originalTitles = []
    for element in root.find("dict").findall("key"):
        originalTitles.append(element.text)
    print(originalTitles)

    name = []
    for element in root.find("dict").findall("dict"):
        name.append(element.find("string").text)
    print(name)

    modifiedTitles = []
    for i in range(0, originalTitles.__len__()):
        newTitle = originalTitles[i].split(FILE_EXTENSION)[0] + " " + name[i] + FILE_EXTENSION
        modifiedTitles.append(newTitle)
    print(modifiedTitles)

    print()

    def isMathingOneOfThose(filename, those):
        for oneOfThose in those:
            if oneOfThose == filename:
                return True
        return False

    try:
        for filename in os.listdir(pathDir):
            if filename.endswith(FILE_EXTENSION) and isMathingOneOfThose(filename, originalTitles):
                os.rename(
                    os.path.join(pathDir, filename),
                    os.path.join(pathDir, modifiedTitles[originalTitles.index(filename)])
                )
    except IOError as e:
        print(e)
        print("Exit by error above.")
        exit()

    print("Nicely done.")
