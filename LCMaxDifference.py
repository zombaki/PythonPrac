def maxDifference(a):
    len_array = len(a)

    diff = a[1] - a[0]
    curr_diff = diff
    maxdiff = curr_diff

    for i in range(1,len_array-1):
        diff = a[i + 1] - a[i]
        if (curr_diff > 0):
            curr_diff += diff
        else:
            curr_diff = diff
        if (curr_diff > maxdiff):
            maxdiff = curr_diff
    return maxdiff
