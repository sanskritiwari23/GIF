import imageio.v3 as iio

filenames = ['WIN_20241230_11_24_25_Pro.jpg', 'WIN_20241230_11_24_27_Pro.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

# import imageio.v3 as iio

# filenames = ['IMG-20240505-WA0065.png', 'IMG_20240102_063733.png']
# images = [ ]

# for filename in filenames:
#   images.append(iio.imread(filename))

# iio.imwrite('team.gif', images, duration = 500, loop = 0)


#Some error occuring, will check afterwards
