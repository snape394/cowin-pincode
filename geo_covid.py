# import math
#
# import geocoder
# from haversine import haversine
import pandas as pd

# from geopy.distance import geodesic
#
# coords_2 = (52.406374, 16.9251681)
#
# pin = 'IN/'+'262701'
df = pd.read_csv('pincode_details.csv')
# my_loc = df.loc[df['key'] == pin].iloc[0]
# coords_1 = ( my_loc['latitude'], my_loc['longitude'])
# for index, row in df.iterrows():
#     lat_1, long_1 = row["latitude"], row["longitude"]
#     if not math.isnan(lat_1):
#         coords_2 = (lat_1, long_1)
#         distance = geodesic(coords_1, coords_2).kilometers
#         if distance < 50:
#             print(row)
#             print('-----------------------')
#             print(distance)
from geopy.geocoders import Nominatim

i = 0
for index, row in df.iterrows():
    city = str(row['pincode'])
    if row['circlename'] == 'Uttar Pradesh':
        geolocator = Nominatim(user_agent="http")
        location = geolocator.geocode(city)
        if location:
            df.loc[index, 'latitude'], df.loc[index, 'longitude'] = location.latitude, location.longitude
            print(row['officename'], ' : ', (location.latitude, location.longitude))


df.to_csv("AllDetails.csv", index=False)
