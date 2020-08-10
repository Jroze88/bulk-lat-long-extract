import csv
import os
from GPSPhoto import gpsphoto
import exifread

with open('locations.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

# points = []
# for r, d, f in os.walk(path):
#     for file in f:
#         if file.lower().endswith(('.png', '.jpg', '.jpeg')):
#             filepath = os.path.join(r, file)
#             exif = get_exif(filepath)
#             if exif is not None and 'GPSInfo' in exif:
#                 latlong = get_decimal_coordinates(exif['GPSInfo'])
#                 if latlong is not None:
#                     points.append(latlong)


count = 0

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if os.path.splitext(file)[-1].lower() == '.jpg' or os.path.splitext(file)[-1].lower() == '.png' or os.path.splitext(file)[-1].lower() == '.tiff' or os.path.splitext(file)[-1].lower() == '.gif' or os.path.splitext(file)[-1].lower() == '.mp4' or os.path.splitext(file)[-1].lower() == '.mpeg' or os.path.splitext(file)[-1].lower() == '.webm':
        # f = open(os.path.join(subdir, file), 'rb')
        # tags = exifread.process_file(f)
        # print get_exif_location(tags)
            tags = gpsphoto.getGPSData(os.path.join(subdir, file))
            count +=1
            spamwriter.write([str(count), file, tags['Lattitude'], tags['Longitude'], tags['Date']])