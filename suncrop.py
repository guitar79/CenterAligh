import os, sys, sun
from PIL import Image

for i in range (1,400):		#image index range

	infile = "img/in/sun-%04d.tif" % i
	outfile = "img/crop/sun-%04d.tif" % i

	im = Image.open(infile)
	print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

	print "Finding sun..."
	imtrim = sun.bbcrop(im, 200)

	print "Saving to %s" % outfile
	imtrim.save(outfile)

print "Done!\n"
