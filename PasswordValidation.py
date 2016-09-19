#Program for password validation

"""                                 swe64dge@het
take password as input
password count to zero
iterate each character by using for
if character is equal to number then increment the password count
once again iterate each character by using if to find out any special character
and increment the password count
print the password count and if it is equal to 2 print valid"""

password=input("enter the password")
passwordCount=0
for passwordchar in password:
	"""if passwordchar in(1,2,3)
		passwordCount+=1
	if passwordchar =="1": #or passwordchar =="2":
		passwordCount+=1	
	if passwordchar =="3": #or passwordchar =="2":
		passwordCount+=1
	if passwordchar=="@":
		passwordCount+=1
if 0<passwordCount<12:
	print "the given password is valid and passwordCount is %s"%passwordCount
else:
	print "the given password is not valid and passwordCount is %s"%passwordCount"""
	#numbers=["0","1","2","3"]
	for passwordchar in range(0,9):
		print passwordchar
		passwordCount+=1
		if passwordchar=="@":
			passwordCount+=1
if 0<passwordCount<12:
	print "the given password is valid and passwordCount is %s"%passwordCount
else:
	print "the given password is not valid and passwordCount is %s"%passwordCount
	
		


