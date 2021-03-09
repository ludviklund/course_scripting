import numpy
import struct
import copy

# 0 = blue, 1 = green, 2 = red

file = open("oslomet.bmp", "rb")

# 1. Read the header of the file and print the size of the picture (height, width) 
header = numpy.fromfile(file, dtype=numpy.uint8, count=54)
img_width = header[18]+header[19]*256+header[20]*(256**2)+header[21]*(256**3)
img_height = header[22]+header[23]*256+header[24]*(256**2)+header[25]*(256**3)
print("Height: {}, width: {}".format(img_height, img_width))

# 2. Read the pixels of the bitmap into a numpy 3D array containing the 3 color components (red, green, blue). First index: row, second index: column, third index: component 
data = numpy.fromfile(file, dtype=numpy.uint8)
rgb_arr = data.reshape(img_height, img_width, 3)
file.close()

# 3. Copy array and change pixels with bvalue > 150 to rgb(255,255,255)
rgb_arr_copy = rgb_arr.copy()
# Change said pixels to white
for i in range(img_height):
    for y in range(img_width):
        if rgb_arr_copy[i, y, 0] > 150 and rgb_arr_copy[i, y, 1] > 150 and rgb_arr_copy[i, y, 2] > 150:
            rgb_arr_copy[i, y, 0] = rgb_arr_copy[i, y, 1] = rgb_arr_copy[i, y, 2] = 255

# Save new picture as copy
snow_img = open("oslomet_snow.bmp", "wb")
header.astype("int8").tofile(snow_img)
rgb_arr_copy.astype("int8").tofile(snow_img)
snow_img.close()

# 4. Copy array and change RGB-pixels where red and green > 130 and blue < 110, swap red and green,
# increase green by 50 if possilbe and decrease red by 50 if possible. 
rgb_arr_copy = rgb_arr.copy()
for i in range(img_height):
    for y in range(img_width):
        if rgb_arr_copy[i, y, 0] < 110 and rgb_arr_copy[i, y, 1] > 130 and rgb_arr_copy[i, y, 2] > 130:
            rgb_arr_copy[i, y, 1], rgb_arr_copy[i, y, 2] = rgb_arr_copy[i, y, 2], rgb_arr_copy[i, y, 1]
            if rgb_arr_copy[i, y, 1] >= 205:
                rgb_arr_copy[i, y, 1] += 50
            else:
                rgb_arr_copy[i, y, 1] = 255
            if rgb_arr_copy[i, y, 2] >= 50:
                rgb_arr_copy[i, y, 2] -= 50
            else:
                rgb_arr_copy[i, y, 2] = 0

# Save new picture as copy
ylw_img = open("oslomet_yellow.bmp", "wb")
header.astype("int8").tofile(ylw_img)
rgb_arr_copy.astype("int8").tofile(ylw_img)
ylw_img.close()

# 5. Cut the uppter 200x200 pixels from both edges. Modify header accordingly.
rgb_arr_copy = rgb_arr[:430, 200:1000]
header_copy = header.copy()
header_copy[18] = 800 % 256
header_copy[19] = 800 / 256
header_copy[22] = 430 % 256
header_copy[23] = 430 / 256

# Save new picture as copy
small_img = open("oslomet_small.bmp", "wb")
header_copy.tofile(small_img)
rgb_arr_copy.tofile(small_img)
small_img.close()



