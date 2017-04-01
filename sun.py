import os, sys
from PIL import Image, ImageOps

def thresh1(x): #zero threshold for finding sunspots
	if x < 60:
		x = 0
	return x

def thresh2(x): #zero threshold for cropping around sun
	if x < 128:
		x = 0
	return x

def bbcrop(image, border):
	box1 = image.point(thresh2).getbbox()
	box2 = (box1[0]-border, box1[1]-border, box1[2]+border, box1[3]+border)
	return image.crop(box2)
