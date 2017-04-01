import os, sys, sun
from PIL import Image

input_image_list = [x.replace('\n','') for x in open('list.txt').readlines()]

for filename in input_image_list:

	infile = 'img/in/' + filename
	outfile = 'img/out/' + filename

	im = Image.open(infile)
	print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

	print "Finding sun..."
	imtrim = sun.bbcrop(im, 200)

	print "Saving to %s" % outfile
	imtrim.save(outfile)

print "Done!\n"
