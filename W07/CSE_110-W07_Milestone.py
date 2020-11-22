from PIL import Image

image_beach = Image.open('images/beach.jpg')

# print(image_beach.size)
# print(image_beach.format)

image_combined = Image.new('RGB', image_beach.size)
(width, height) = image_beach.size
print(f'Width: {width}')
print(f'Height: {height}')

pixels_beach = image_beach.load()

# print(pixels_beach[200, 100])

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_beach[x, y]

        new_blue = b + 100
        new_red = r + 100
        new_green = g + 100

        pixels_beach[x, y] = (r, g, new_blue)

image_beach.show()
image_beach.save('beach_blue_tint.jpg')