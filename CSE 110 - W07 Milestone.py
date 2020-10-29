from PIL import Image

image_beach = Image.open('images/beach.jpg')

pixels_beach = image_beach.load()
(width, height) = image_beach.size


for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_beach[x, y]

        new_blue = b + 100
        new_red = r + 100
        new_green = g + 100

        pixels_beach[x, y] = (new_red, g, b)

image_beach.show()
