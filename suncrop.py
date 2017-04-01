import os, sys, sun
from PIL import Image

input_image_list = os.listdir('img/in/')

for filename in input_image_list:
	if(filename[-4:] != '.JPG'): # skip file if it's not image file
		continue

	infile = 'img/in/' + filename
	outfile = 'img/out/' + filename

	im = Image.open(infile)
	print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

	print "Finding sun..."
	imtrim = sun.bbcrop(im, 200)

	print "Saving to %s" % outfile
	imtrim.save(outfile)

print "Done!\n"
