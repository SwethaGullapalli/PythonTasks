# Program to find indexes of the Alphabetslist

"""Give input as Alphabetslist 
iterate each alphabetlist in Alphabetslist
		initialize index of a and index of b
		iterate each alphabet in the alphabetlist
			if "a"==each alphabet
			increment the count of a
			print the count of a
			if "b"=each alphabet
			increment the count of b
			print the count of b"""
			

ListOfAlphabets = ["aabc","bbcde"]

"""print ListOfAlphabets[1]


#for AlphabetList in ListOfAlphabets:
IndexOfa=0
IndexOfb=0
for EachAlphabet in ListOfAlphabets[0]:
	if "a" == EachAlphabet:
		IndexOfa+=1	
for EachAlphabet in ListOfAlphabets[1]:
	if "b"== EachAlphabet:
		IndexOfb+=1
print"The number of b's in the second list is %s"%IndexOfb	
print"The number a's the first list is %s"%IndexOfa"""

IndexOfa=0
IndexOfb=0
for EachAlphabet in ListOfAlphabets[0]:
    if EachAlphabet[1] == "a":
		IndexOfa+=1
	if EachAlphabet[2] == "b":
		IndexOfb+=1
		
for EachAlphabet in ListOfAlphabets[1]:
	if EachAlphabet[1] == "a":
		IndexOfa+=1	
	if EachAlphabet[2] == "b":
		IndexOfb+=1
print "the number of a's in first index is %s"%IndexOfa
print "the number of b's in second index is %s"%IndexOfb
	
	
	


			
			
		