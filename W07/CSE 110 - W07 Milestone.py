from PIL import Image

image_desert = Image.open('images/desert.jpg')


pixels_desert = image_desert.load()

(width, height) = image_desert.size

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_desert[x, y]

        new_blue = b + 100
        new_red = r + 100
        new_green = g + 100

        pixels_desert[x, y] = (new_red, g, b)

image_desert.show()

