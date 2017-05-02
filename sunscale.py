import os, sys, sun
from PIL import Image, ImageOps

f = open("errorlog.txt","a")

def do_sunscale(filename, dir1, dir2):

	infile = "img/" + dir1 + "/" + filename
	outfile = "img/" + dir2 + "/" + filename
	try:
		outdims = (1920,1080)
		imout = Image.new("RGB",outdims,0)
		im = Image.open(infile)
		# print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

		print "Scaling..."
		mindim = min(outdims)
		im = sun.bbcrop(im, 100)
		im = ImageOps.fit(im, (mindim,mindim), Image.ANTIALIAS, 0, (0.5,0.5))
		imout.paste(im, ( ((imout.size[0]-im.size[0])/2) ,0))

		# print "Saving to %s" % outfile
		imout.save(outfile)
	except:
		print "Error occured while processing %s" % (infile)
		f.write("%s\n" % (infile))