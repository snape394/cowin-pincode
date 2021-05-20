import time

from flask import Flask
from geopy.geocoders import Nominatim
import pandas as pd
import os.path
from os import path

app = Flask(__name__)


@app.route('/')
def server():
    return 'Server Running'

# @app.route('/getcoordinates')
# def server():
#     df = pd.read_csv('all-details.csv')
#     return 'Server Running'

@app.route('/start')
def start():
    if not path.exists("all-details.csv"):
        df = pd.read_csv('pincode_details.csv')
        for index, row in df.iterrows():
            city = str(row['pincode'])
            if row['circlename'] == 'Uttar Pradesh':
                geolocator = Nominatim(user_agent="http")
                location = geolocator.geocode(city)
                if location:
                    df.loc[index, 'latitude'], df.loc[index, 'longitude'] = location.latitude, location.longitude
                    print(row['officename'], ' : ', (location.latitude, location.longitude))
        df.to_csv("all-details.csv", index=False)

    return 'Completed'


if __name__ == '__main__':
    app.run(debug=True, threaded=True)