import os
import shutil

Folderpath1=raw_input("please enter first folder name : ")
Folderpath2=raw_input("please enter second folder name : ")
needmatchedfiles=raw_input("do you want matched files? ")
needmatchedfiles=needmatchedfiles=="yes"
donotneedmatchedfiles=raw_input("do you want unmatched files? ")
donotneedmatchedfiles=donotneedmatchedfiles=="yes"

print needmatchedfiles
print donotneedmatchedfiles
list1=[]
list2=[]
matchedlist=[]
unmatchedlist=[]
if os.path.isdir(Folderpath1):
	print "This is a folder1"
	Folderfiles1=os.listdir(Folderpath1)
	print Folderfiles1
if os.path.isdir(Folderpath2):
	print "This is a folder2"
	Folderfiles2=os.listdir(Folderpath2)
	print Folderfiles2
for Filename1 in Folderfiles1:
	if os.path.isfile(Folderpath1 +'\\'+ Filename1):
		list1.append(Filename1)
for Filename2 in Folderfiles2:
	if os.path.isfile(Folderpath2 + "\\"+ Filename2):
		list2.append(Filename2)

for i in list1:#a.txt,b.txt
	for j in list2:#c.txt,d.txt,a.txt
		if needmatchedfiles:
			if i==j:
				matchedlist.append(i)
			else:
				if  i not in unmatchedlist :
					unmatchedlist.append(i)
				if j not in unmatchedlist :
					unmatchedlist.append(j)
if needmatchedfiles:
	print "List is Matched and the matched list is %s"%matchedlist
if donotneedmatchedfiles:
	print"List is not matched and the unmatched list is %s"%unmatchedlist
					
		


