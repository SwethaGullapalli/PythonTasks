# program to find number of repititions of a letter in the given word
"""
give input as a string
for counting the number of repititions initialize a variable
write for loop for each character in the string
equate the variable declared in for loop to the letter repititions
increment the variable used for repetitions
print the variable
"""
"""T="MISSISSIPPI"
C=0
for i in T:
	if i=="S":
		C+=1  #IT MEANS C=C+1
print "The number of repititions is %s"%C"""
		
#same program but input should be taken from the user


count=0
inputString = raw_input("Enter the word: ");
repCharacter = raw_input("Character to check: ")
for char in inputString: 
	if char == repCharacter:
		count += 1  #IT MEANS C=C+1
print "The number of repititions is %s"%count

 

