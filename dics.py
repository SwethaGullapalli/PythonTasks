# dictionaries program

dict1={"hyd":1234,("chennai","sec"):467,"mumbai":[234,123],"sikkim":965,2967:"bhopal"}
print dict1.keys()
print dict1.values()
#dict2={}
#dict2.update(dict1)
#print dict2
#print list(dict1)
#print sorted(dict1,key=str.upper)
#print sorted(dict1.values())
#for key in dict1.itervalues():
#	print key[0]
	#print value
print dict1[2967]
# TASK----------------->>> print dict1.keys()[dict1.values().index(467)]



# dictionaries to list conversion

a=[1,2,3,4,5,6,7,8]
d={}
j=0
print len(a)
for i in a:
	if j+1>len(a):
		break
	d[a[j]]=a[j+1]
	j=j+2	
print d
		







