#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image

input_file = "input.png"	# used to generate hexadecimal numbers
output_file = "output.txt"	# stores all the hexadecimal numbers in the right format
byte = 8

def process_image(width, height, height_in_pages):
	hex_result = ""
	for y1 in range(height_in_pages):
		for x in range(width):
			binary = ""
			for y2 in range(7, -1, -1):
				y = y2 + (y1 * byte)
				color_array = img.getpixel((x, y))
				if (color_array == (255, 255, 255)) or (color_array == (255, 255, 255, 255)):	# check whether RGB/RGBA color value of a particular pixel is white
					binary += "0"
				else:
					binary += "1"
			hex_value = hex(int(binary, 2))
			if len(hex_value) == 3:
				hex_value = hex_value[:2]+"0"+hex_value[2:]
			hex_result += str(hex_value+",")
	return(hex_result)

def write_to_file(result):
	file = open(output_file, "w")
	file.write(result+"\n")
	file.close

try:
	img = Image.open(input_file)
except:
	print("Error: "+input_file+" could not be found!")
	exit()

width = img.size[0]			# read width of input file
height = img.size[1]			# read height of input file (32px max.)
height_in_pages = height / byte		# the Tiny4kOLED library only allows four Y values in the form of 8 bit RAM pages

print("Image dimensions are "+str(width)+" x "+str(height)+" pixels.")
print("Image height in RAM pages is "+str(int(height_in_pages))+".")

if (height_in_pages == int(height_in_pages)) and (height <= 32):	# check whether the image has proper dimensions
	height_in_pages = int(height_in_pages)
	print("Processing image...")
	result = process_image(width, height, height_in_pages)
	try:
		write_to_file(result)
		print("Hexadecimal values have successfully been written to "+output_file+"!")
	except:
		print("Unable to access "+output_file+". Check file permissions!")
else:
	print("Error: Image height must be a multiple of 8 and may not be greater than 32!")
	exit()
