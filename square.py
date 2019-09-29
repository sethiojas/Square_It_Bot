from PIL import Image
import os

def square_image(filename):
	''' 
	Squares the image whose path is received.
	The padding is kept white.
	'''
	im = Image.open(filename)
	size = max(im.size)
	x, y= im.size

	new_im = Image.new('RGB', (size, size), (255, 255, 255))
	new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
	im.close()
	os.remove(filename)
	new_im.save(filename)
	new_im.close()