import os
import re
import sys

#RenameFile.py
#Coder: suoiviet
#Description: This script serves to rename all files within a directory ("source"). 
#The new filenames are generated dynamically by a template & a number sequence specified by the user.  

#USER NEED TO CHANGE THESE*****************************************
#Template for changing the filename into
#need to change sTemplate's value to a desired filename format. Need to use "#" where the filename is sequenced. Multiple "#" indicates zero padded numbers
#iStart is the start number of the sequence 

#Examples---------
#sTemplate = "Today#.txt" 
#iStart = 1
## file.txt, fileA.txt will rename to Today1.txt, Today2.txt

#sTemplate = "AsToday##.txt"
#iStart = 0
## file.txt, fileA.txt will rename to AsToday01.txt, AsToday02.txt

#sTemplate = "Example###.log"
#iStart = 15
## file.txt, fileA.txt will rename to Example015.log, Example016.log, etc...

sTemplate = "#XYZ.txt"
iStart = 2
#***************************************************************

#sort files alphanumerically
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#find position of # in sTemplate
iCntPound = sTemplate.count('#')
if iCntPound < 1:
    sys.exit("Error: '#' is required in the template")

iFirst = sTemplate.find("#")
iLast = sTemplate.rfind("#")
sPound =  sTemplate[iFirst:iLast+1]

#get files in source
dirFiles = os.listdir("./source") #list of directory files in "source" of current directory
dirFiles = sorted(dirFiles, key=numericalSort)
i=iStart
for filename in dirFiles:
    #print(filename)

    #.gitignore in "source" & "destination" are ignored. It is used for ignoring local repository from uploading onto github
    if filename == ".gitignore":
        continue

    #get number in sequence, pad 0s if multi # in sTemplate
    sPadNumber = str(i).zfill(iCntPound)
    #create new filename
    newFileName =sTemplate.replace(sPound, sPadNumber)
    #move files from "source" to "destination"
    os.replace("./source/"+filename, "./destination/"+newFileName)

    i+=1


print("Finished!")
print("Total number of files renamed: "+str(i-iStart))