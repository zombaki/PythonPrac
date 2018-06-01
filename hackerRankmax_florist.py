def  max_florists(path_length, florist_intervals):
    path_array = []
    count = 0
    florist_intervals.sort(key=lambda x: x[1]-x[0])
    print florist_intervals
    for i in range(0,path_length+1):
        path_array.append(0)
    for intervals in florist_intervals:
        florist = True
	if intervals[0]>path_length:
		florsit=False
		break
        for i in range(intervals[0],intervals[1]):
		if path_array[i] <3:
                    path_array[i] += 1
                else:
                    florist = False
                    break
        if florist:
            count += 1
    return count

print max_florists(9,[(1,10),(1,6),(2,8),(3,5)])
