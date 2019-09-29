from PIL import Image
import os

def square_image(filename, colour):
	''' 
	Squares the image whose path is received.
	The padding is according to the user choice.
	'''
	im = Image.open(filename)
	size = max(im.size)
	x, y= im.size
	if colour.lower() == "white":
		RGB = (255, 255, 255)
	else if colour.lower() == "black":
		RGB = (0, 0, 0)
	else:
		red = 0
		green = 0
		blue = 0
		count = 0

		for r,g,b in im.getdata():
			red = red + r
			blue = blue + b
			green = green + g

		red = int(red/count)
		blue = int(blue/count)
		green = int(green/count)

		RGB = (red, green, blue)

	new_im = Image.new('RGB', (size, size), RGB)
	new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
	im.close()
	os.remove(filename)
	new_im.save(filename)
	new_im.close()