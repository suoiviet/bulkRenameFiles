# Bulk Rename Files
This python script rename all files in a directory. The files are renamed sequencially.

The user of the script specifies a template, in which all files are renamed into. This template needs to contain the character(s) "#". It serves as a placeholder for the numeric sequence of the files. The user also has to specify a "start number" for the sequence.

Cloning this repository should download this README.md, bulkRenameFiles.py, empty "source" and "destination" subfolders

## Executing the script
1. Make sure you have these installed
	- Python
2. Put all files you want to rename in the "source" subfolder 
3. Go into bulkRenameFiles.py, change the variables sTemplate and iStart to your requirements (see Examples below)
3. Open Terminal and change the directory to the location of bulkRenameFiles.py. Run bulkRenameFiles.py (there exists different syntaxes for executing Python scripts, depending on the Python version and OS you're running on)
4. When the script finished, the new files will be generated in "destination" subfolder

## Examples (to be put inside bulkRenameFiles.py)
sTemplate = "Today#.txt" 
iStart = 1
// file.txt, fileA.txt will rename to Today1.txt, Today2.txt

//Using multiple #, zero(S) are left-padded to the numbers. ## is for 2 characters padding, ### is 3 characters, etc...
sTemplate = "AsToday##.txt"
iStart = 0
// file.txt, fileA.txt will rename to AsToday01.txt, AsToday02.txt

sTemplate = "Example###.log"
iStart = 15
<<<<<<< HEAD
// file.txt, fileA.txt will rename to Example015.log, Example016.log, etc....
=======
// file.txt, fileA.txt will rename to Example015.log, Example016.log, etc....
>>>>>>> 43a3a3836865a9a91812cfae5b73378cfbc1957f
