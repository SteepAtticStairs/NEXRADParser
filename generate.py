#!/usr/bin/python
import level3_to_png

# radar_file, lat_min, lat_max, lon_min, lon_max, x_res, y_res
file = 'data/LWX_N0Q_2022_04_18_15_21_24'
output = 'radar.png'
lat_min = '34'
lat_max = '42'
lon_min = '-82'
lon_max = '-72'
x_res = 2048
y_res = x_res

image = level3_to_png.level3_to_png(file, lat_min, lat_max, lon_min, lon_max, x_res, y_res)
image.save(output)