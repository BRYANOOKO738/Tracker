import folium.map
import phonenumbers
from phonenumbers import geocoder
import folium
from test import number

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)
print(check_number)
 
from phonenumbers import carrier
service_provider =phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))
KEY="ecca9e5d6eb94c3981daf19dd025835b"
from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(KEY)

query =str(number_location)

results = geocoder.geocode(query)

lat = results[0]["geometry"]["lat"]

lng = results[0]["geometry"]["lng"]

print(lat, lng)

map_location = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=folium.Popup(str(number_location))).add_to(map_location)


map_location.save("myLocation.html")

