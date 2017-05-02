import os, sys, sun
from PIL import Image

f = open("errorlog.txt","a")

def do_suncrop(filename, dir1, dir2):

	infile = "img/" + dir1 + "/" + filename
	outfile = "img/" + dir2 + "/" + filename

	try:
		im = Image.open(infile)
		# print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

		print "Cropping..."
		imtrim = sun.bbcrop(im, 200)

		# print "Saving to %s" % outfile
		imtrim.save(outfile)
	except:
		print "Error occured while processing %s" % (infile)
		f.write("%s\n" % (infile))
