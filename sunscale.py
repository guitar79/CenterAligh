import os, sys, sun
from PIL import Image, ImageOps

for i in range (1,400):		#image index range

	infile = "img/rot/sun-%04d.tif" % i
	outfile = "img/scale/sun-%04d.tif" % i

	outdims = (1920,1080)
	imout = Image.new("RGB",outdims,0IImage.open(infile)
	print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

	print "Scaling..."
	mindim = min(outdims)
	im = sun.bbcrop(im, 100)
	im = ImageOps.fit(im, (mindim,mindim), Image.ANTIALIAS, 0, (0.5,0.5))

	print "Framing..."
	imout.paste(im, ( ((imout.size[0]-im.size[0])/2) ,0))

	print "Saving to %s" % outfile
	imout.save(outfile)

print "Done!\n"
