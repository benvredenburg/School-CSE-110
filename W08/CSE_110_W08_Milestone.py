from PIL import Image

image_desert = Image.open('images/desert.jpg')
image_cactus = Image.open('images/cactus.jpg')
image_cat = Image.open('images/cat_small.jpg')
image_hiker = Image.open('images/hiker.jpg')

pixels_desert = image_desert.load()
pixels_cactus = image_cactus.load()
pixels_cat = image_cat.load()
pixels_hiker = image_hiker.load()

(width, height) = image_desert.size

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cat[x, y]

        if g < 150:
            new_blue = b + 100
            new_red = r + 100
            new_green = g + 100

            pixels_cat[x, y] = (new_red, g, b)

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_hiker[x, y]

        if g < 150:
            new_blue = b + 100
            new_red = r + 100
            new_green = g + 100

            pixels_hiker[x, y] = (r, g, new_blue)

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cactus[x, y]

        if r < 150 and b < 150 and g > 100:
            pixels_cactus[x, y] = pixels_hiker[x - 100, y]

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cactus[x, y]

        if r < 150 and b < 150 and g > 100:
            pixels_cactus[x, y] = pixels_cat[x, y]

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cactus[x, y]
        if r < 100 and b < 100 and g > 150:
            pixels_cactus[x, y] = pixels_desert[x, y]



# image_cactus.save('W08Milestone.jpg')
image_cactus.show()
