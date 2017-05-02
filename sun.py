import os, sys
from PIL import Image, ImageOps

EPS = 60

def thresh(x): #zero threshold for finding sunspots
	if x < EPS:
		x = 0
	return x

def bbcrop(image, border):
	box1 = image.point(thresh).getbbox()
	box2 = (box1[0]-border, box1[1]-border, box1[2]+border, box1[3]+border)
	return image.crop(box2)
