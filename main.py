import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
key = '64ab9397459249f793e1f22adc74c244'

#To show the country name (CH=country history)
samNumber = phonenumbers.parse(number)
yourlocation = geocoder.description_for_number(samNumber, "en")
print(yourlocation)

#To show the service provider of the number
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))


# To get the latitude and longitude of the number
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourlocation)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

# Displaying Location on the map

myMap = folium.Map(location=[lat, lng], zoom_start=10)

folium.Marker([lat, lng], popup=yourlocation).add_to((myMap))

##saving Map as HTML file
myMap.save("Mylocation.html")