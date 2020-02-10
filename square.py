from PIL import Image
import os

def square_image(filename, colour):
	''' 
	Squares the image whose path is received.
	The padding is according to the user choice (Black/White).
	'''
	
	im = Image.open(filename)
	size = max(im.size)
	x, y= im.size
	
	if colour.lower() == "white":
		RGB = (255, 255, 255)
	elif colour.lower() == "black":
		RGB = (0, 0, 0)

	new_im = Image.new('RGB', (size, size), RGB)
	new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
	
	im.close()
	os.remove(filename)
	
	new_im.save(filename)
	new_im.close()