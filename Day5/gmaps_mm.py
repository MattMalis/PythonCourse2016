# pip install googlemaps
#https://console.developers.google.com/apis/credentials?project=_
#need maps and distance APIs enabled
import googlemaps
api_key = 'your api key from developers.google.com'
gmaps = googlemaps.Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location=gmaps.geocode(whitehouse)
print location
print location[0]
print location[0]['geometry']['location']
latlng=location[0]['geometry']['location']
lat, lng=latlng.values()

destination = gmaps.reverse_geocode(latlng)
print destination 

duke = gmaps.geocode('326 Perkins Library, Durham, NC 27708')
duke=duke[0]['geometry']['location']
distance = gmaps.distance_matrix(duke, latlng)
distance['rows'][0]['elements'][0]['distance']['text']
distance['rows'][0]['elements'][0]['distance']['value']


embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

emb_dicts = []
for item in embassies:
	cur_dict = {'lat':item[0], 'lng':item[1]}
	emb_dicts.append(cur_dict)

emb_dist01 = gmaps.distance_matrix(emb_dicts[0], emb_dicts[1])
emb_dist02 = gmaps.distance_matrix(emb_dicts[0], emb_dicts[2])
emb_dist12 = gmaps.distance_matrix(emb_dicts[1], emb_dicts[2])


class CustomException(Exception): 
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value




#### FUNCTION TO FIND DISTANCES FROM A DESTINATION
## takes as arguments: a list of length 2, for the destination's lat/lng;
##		and a list of lists of length 2, for each comparison point's lat/lng
## returns: a list of distances from comparison points to destination
## 			(in the order in which they were provided)
def dist_from_dest(dest_lat_lng, list_other_lat_lngs):
	usage_message = """function takes arguments: dest_lat_lng = list of length 2,
			list_other_lat_lngs= list of lists of length 2;
			function returns list of distances (in meters) from other_lat_lngs to dest"""
	if not isinstance(dest_lat_lng, list):
		raise CustomException(usage_message)
	if len(dest_lat_lng)!=2:
		raise CustomException(usage_message)
	for item in list_other_lat_lngs:
		if len(item)!=2:
			raise CustomException(usage_message)
	dicts = []
	for item in list_other_lat_lngs:
		cur_dict = {'lat':item[0], 'lng':item[1]}
		dicts.append(cur_dict)
	dest_dict = {'lat':dest_lat_lng[0], 'lng':dest_lat_lng[1]}
	distances = []
	for this_dict in dicts:
		this_dist = gmaps.distance_matrix(this_dict, dest_dict)
		this_value = this_dist['rows'][0]['elements'][0]['distance']['value']
		distances.append(this_value)
	return distances

#### getting embassy address:
emb1_address=gmaps.reverse_geocode(embassies[0])
emb1_address_clean = emb1_address[0]['formatted_address']

### generalizing to a a function...
def get_clean_address(lat_lng):
	address_messy = gmaps.reverse_geocode(lat_lng)
	address_clean = address_messy[0]['formatted_address']
	return address_clean

#### FUNCTION FOR FINDING NEARBY PLACES
def find_nearby(search_term, lat_lng_list): ## lat_lng is a list of length 2, [lat,lng]
	places_all = gmaps.places(search_term, lat_lng_list)
	places = places_all['results']
	name_address_lat_lng_dicts = []
	for place in places:
		name = place['name']
		cur_dict = {name:[]}
		lat_lng_dict = place['geometry']['location']
		address = place['formatted_address']
		cur_dict[name].append(address)
		cur_dict[name].append(lat_lng_dict)
		name_address_lat_lng_dicts.append(cur_dict)
	return name_address_lat_lng_dicts

# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? You will get errors - debug
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

