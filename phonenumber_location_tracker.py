import phonenumbers
from phonenumbers import carrier,geocoder,timezone

number="+19999999999"
parsed_num = phonenumbers.parse(number)
number_location = geocoder.description_for_number(parsed_num,"en")
print(number_location)


#service_provider = phonenumbers.parse(number)
#print(carrier.name_for_number(service_provider, "en"))

#from opencage.geocoder import OpenCageGeocode
#geocoder = OpenCageGeocode(Key)

#query = str(number_location)
#results = geocoder.geocode(query)

#lat = results[0]['geometry']['lat']
#lng = results[0]['geometry']['lng']
#print(lat,lng)


