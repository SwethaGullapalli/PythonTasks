#program to print the file extension having py

"""give input as list of file names
iterate each file name in file names list
	declare one variable for holding file extension
	declare variables for index and dot index
	iterate each character in the file name
		increment the index by 1
		if Character is equal to "." assign index to dot index
		if index is greater than or equal to dot index 
			concatenate the character to file extension variable
	if .py== file extension variable
			print file name"""
			
			
FileNameList = ["blue.py","black.txt","orange.log","red.py"]	
for FileName in FileNameList:
	FileExtension=""
	Index =0
	DotIndex = -1
	for Character in FileName:
		if Character == ".":
			DotIndex = Index
		if Index>=DotIndex and DotIndex!=-1:
			FileExtension=FileExtension+Character
		Index+=1
	if".py" == FileExtension:
		print FileName
	

			
			
	