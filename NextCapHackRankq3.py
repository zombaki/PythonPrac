def strengthen_passwords(passwords):
	res = list()
	for i in passwords:
		if "s" in i:
			i = i.replace("s", "5")

		if "S" in i:
			i = i.replace("S", "5")

		middleIndex = len(i)/2
		if len(i)%2 != 0 and i[len(i)/2].isdigit() and len(i)>1:
			a = i[middleIndex]
			b = int(a) * 2
			i = i[:middleIndex] + str(b) + i[middleIndex+1:]

		if len(i)%2 == 0:
			if ord(i[-1]) <97 and ord(i[0])>=97:
				i = i[-1].lower() + i[1:-1] + i[0].upper()
			elif ord(i[-1])>=97 and ord(i[0])< 97:
				i = i[-1].upper() + i[1:-1] + i[0].lower()
			else:
				i = i[-1] + i[1:-1] + i[0]

		if i.lower().find('nextcapital') is not -1:
			startIndex = i.lower().index('nextcapital')
			#i = i[:startIndex] +  i[startIndex:startIndex+4:-1]   + i[startIndex+4:]
			print startIndex
			a= i[startIndex:startIndex+4:]
			print a[::-1]
		res.append(i)
	return res

print strengthen_passwords(["aas",'aaxnextcapitalasd'])
