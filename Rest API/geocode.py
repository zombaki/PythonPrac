import httplib2
import json

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyBW0y_y63XDNQ-0U7ajIpJc5qUJs5vvWSw"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    #result = json.loads(h.request(url,'GET')[1])
    #print h.request(url,'GET')[0]
    latitude = "40.724"#result['results'][0]['geometry']['location']['lat']
    longitude = "-74.0018"#result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

foursquare_client_id = "U2BSE2JYMBD1NFZBTPYZLA1SY202GQ0TLZHFH4SEXXJM40YQ"
foursquare_client_secret = "K3BXKZES4JAR0BMHJGWB42I5F40NOBESSIJQUDJLN4BNC3DT"


"""def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	latitude, longitude = getGeocodeLocation(location)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	
	if result['response']['venues']:
		#3.  Grab the first restaurant
		restaurant = result['response']['venues'][0]
		venue_id = restaurant['id'] 
		restaurant_name = restaurant['name']
		restaurant_address = restaurant['location']['formattedAddress']
		address = ""
		for i in restaurant_address:
			address += i + " "
		restaurant_address = address
		#4.  Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
		url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
		result = json.loads(h.request(url, 'GET')[1])
		#5.  Grab the first image
		if result['response']['photos']['items']:
			firstpic = result['response']['photos']['items'][0]
			prefix = firstpic['prefix']
			suffix = firstpic['suffix']
			imageURL = prefix + "300x300" + suffix
		else:
			#6.  if no image available, insert default image url
			imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
		#7.  return a dictionary containing the restaurant name, address, and image url
		restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
		print "Restaurant Name: %s" % restaurantInfo['name']
		print "Restaurant Address: %s" % restaurantInfo['address']
		print "Image: %s \n" % restaurantInfo['image']
		return restaurantInfo
	else:
		print "No Restaurants Found for %s" % location
		return "No Restaurants Found"
"""
def findARestaurant(Type,location):
	latitude,longitude = getGeocodeLocation(location)
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%sclient_secret=%s&v=20180323&ll=%s,%s&query=%s&limit=1'% (foursquare_client_id,foursquare_client_secret,latitude,longitude,Type))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	if result['response']['venues']:
		restraunt=result['response']['venues'][0]
		venue_id = restraunt['id']
		
	print result

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	#findARestaurant("Tacos", "Jakarta, Indonesia")
	#findARestaurant("Tapas", "Maputo, Mozambique")
	#findARestaurant("Falafel", "Cairo, Egypt")
	#findARestaurant("Spaghetti", "New Delhi, India")
	#findARestaurant("Cappuccino", "Geneva, Switzerland")
	#findARestaurant("Sushi", "Los Angeles, California")
	#findARestaurant("Steak", "La Paz, Bolivia")
	#findARestaurant("Gyros", "Sydney Australia")

