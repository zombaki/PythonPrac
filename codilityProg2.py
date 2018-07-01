def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    print d
    #print l
    for p in range(1, 1 + l/2):
        ok = True
	print l-p
        for i in range(l - p):
            if d[i] != d[i + p]:
		print i+p,'Break ho ra'
                ok = False
                break
        if ok:
            return p
    return -1

if __name__=='__main__':
	print solution(109)
