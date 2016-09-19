

employeeList = ["123 rahul 9.5 8.1 7.6 3.1 3.2","456 Bunny 7.0 9.6 6.5 4.9 8.8","789 sunil 8.0 8.0 8.0 8.0 7.5"]

for employee in employeeList:
	totalHrs = 0.0;
	averageHrs = 0.0;
	empname = ""
	empDetails = employee.split(' ')
	empname = empDetails[1]
	idnumber = empDetails[0]
	totalHrs = float(empDetails[2]) + float(empDetails[3]) + float(empDetails[4]) + float(empDetails[5]) + float(empDetails[6])
	averageHrs = totalHrs/5;
	print ("{0} (ID:{3} ) worked for {1} hours this week with average of {2} hours per day".format(empname, totalHrs, averageHrs,idnumber))
	