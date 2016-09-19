"""give the input as list
iterate each element in list
	check if second character is "L"
		print the second character"""

colorsList = ["blue","black","orange"]
for color in colorsList:
	if color[1] == "l":
		print "The second letter of %s color is l" %color
		