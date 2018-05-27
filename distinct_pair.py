def distinct_pairs(a, k):

    n = len(a)

    pairs = []

    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] + a[j] == k:
                temp = []
		if (a[i]<a[j]):
			temp.append(a[i])
                	temp.append(a[j])
		else:
			temp.append(a[j])
                	temp.append(a[i])
		
                pairs.append(temp)
    print set(pairs)
    return len(pairs)


array_a = [1, 2, 3, 6, 7, 8, 9, 1]
k = 10

print(distinct_pairs(array_a, k))
