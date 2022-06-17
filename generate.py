#!/usr/bin/python
import json
from urllib.request import urlopen
import level3_to_png

'''
Fetches a master json of all of the bounding boxes,
allowing the user to get a bounding box just by
specifying a radar station.
'''
# https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
url = "https://steepatticstairs.github.io/weather/json/boundingBoxes.json"
# store the response of URL
response = urlopen(url)
# storing the JSON response from url in data
data_json = json.loads(response.read())

# radar_file, lat_min, lat_max, lon_min, lon_max, x_res, y_res
file = 'data/LWX_N0B_2022_06_17_00_50_49'
output = 'radar.png'
station = 'KLWX'
lat_min = data_json[station][0]
lat_max = data_json[station][1]
lon_min = data_json[station][2]
lon_max = data_json[station][3]
resolution = 2048
x_res = resolution
y_res = resolution

image = level3_to_png.level3_to_png(file, lat_min, lat_max, lon_min, lon_max, x_res, y_res)
image.save(output)