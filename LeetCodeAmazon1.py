def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    	result_local= [(foregroundAppList[i][0], backgroundAppList[j][0],foregroundAppList[i][1]+backgroundAppList[j][1]) for i in xrange(len(foregroundAppList)) for j in xrange(len(backgroundAppList))]
        result_local.sort(key=lambda x: x[2],reverse=True)
        res=[]
        localhigh=0
        for k, v,pri in result_local:
                if pri<=deviceCapacity:
                        if localhigh<> 0 and pri == localhigh:
                                res.append([k,v])
                        elif localhigh==0:
                                res.append([k,v])
                                localhigh=pri
                        else:
                                break
        return res

print optimalUtilization(10,[[1,2],[2,3]],[[1,2]])
