def electionWinner(votes):
	collection = set(votes)

	#print collection
	j , max = 0, 0
	for i in sorted(collection)[::-1]:
		#print i
		if max < votes.count(i):
			max = votes.count(i)
			j = i
	return j
print electionWinner(['zlex','mike','zlex','zlex','zlex'])
