'''class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d={}
        for i in cpdomains:
	    #print i
            li=i.split()
	    #print li
            for b in li[1].split('.'):
		#print b
		d[b]=d.get(b,0)+int(li[0])
		#print d
        return ["{} {}".format(value, key) for key, value in d.iteritems()]
a = Solution()
priint a.subdomainVisits(["9001 discuss.leetcode.com"])'''
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for item in cpdomains:
            cnt, domain = item.split(' ')
            subdomain = domain.split('.')
            for i in xrange(len(subdomain)):
                name = '.'.join(subdomain[i:])
                if name not in dic:
                    dic[name] = int(cnt)
                else:
                    dic[name] += int(cnt)
        return ['{} {}'.format(dic[key], key) for key in dic]
                
