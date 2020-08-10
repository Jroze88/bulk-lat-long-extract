import os
import csv
points = []
names = []
count = -1 
# (-1) to make the array iterator match the number instead of making two variables
for r, d, f in os.walk(path):
    for file in f:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.mpeg', '.mp4', '.mpg')):
            filepath = os.path.join(r, file)
            exif = get_exif(filepath)
            if exif is not None and 'GPSInfo' in exif:
                latlong = get_decimal_coordinates(exif['GPSInfo'])
                names.append(file)
                count +=1
                if latlong is not None:
                    points.append(latlong)
with open('locations.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([str(count), file, points[count]])