import httplib2
import json

def getRoasterDetails():
	url = ('https://api.myjson.com/bins/16roa3')
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	"""if result['response']['venues']:
					restraunt=result['response']['venues'][0]
					venue_id = restraunt['id']
					"""
	print result
if __name__ == '__main__':
	getRoasterDetails()