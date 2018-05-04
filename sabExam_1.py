def temperature(s):
	if (s>90):
		return "it's hot"
	elif(s<60):
		return "it's cold"
	else:
		return "looking good"
input=0
while(1):
	input=raw_input("Enter The Current Temp!! enter -1 to Exit\n")
	try:
		if (input=='-1'):
			break
		val = int(input)
		print temperature(val)
	except ValueError:
   		print("Enter Data is not Int, Please Enter a Integer Value!" 
	

