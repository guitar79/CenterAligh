import os, sys, math, sun
from PIL import Image, ImageOps
from scipy import ndimage
import numpy as np

f = open("errorlog.txt","a")

def findspot(cboxctr, cboxsize, shrinkboxsize, maxiter):

	cboxtl = ((cboxctr[0]-int(cboxsize[0]/2)) , (cboxctr[1]-int(cboxsize[1]/2)))
	cboxbr = ((cboxctr[0]+int(cboxsize[0]/2)) , (cboxctr[1]+int(cboxsize[1]/2)))

	cropbox = (cboxtl + cboxbr)
	ccrop = imthresh.crop(cropbox)

	#ccrop.show()

	done = 0
	shrunk = 0
	iteration = 0
	prescom = (-1,-1)
	while done == 0:

		carr = np.array(ccrop)
		com = ndimage.measurements.center_of_mass(carr)
		abscom = ( int(cboxtl[0]+com[1]) , int(cboxtl[1]+com[0]) )

		if abscom != cboxctr:

			cboxctr = (abscom[0], abscom[1])
			cboxtl = ((cboxctr[0]-int(cboxsize[0]/2)) , (cboxctr[1]-int(cboxsize[1]/2)))
			cboxbr = ((cboxctr[0]+int(cboxsize[0]/2)) , (cboxctr[1]+int(cboxsize[1]/2)))

			cropbox = (cboxtl + cboxbr)
			ccrop = imthresh.crop(cropbox)

			#ccrop.show()	#for debugging

			iteration += 1
			if iteration >= maxiter:
				print "%s: Max iterations reached!" % infile
				sys.exit()
				done = 1

		elif shrunk == 0:

			cboxsize = shrinkboxsize
			cboxctr = (abscom[0], abscom[1])
			cboxtl = ((cboxctr[0]-int(cboxsize[0]/2)) , (cboxctr[1]-int(cboxsize[1]/2)))
			cboxbr = ((cboxctr[0]+int(cboxsize[0]/2)) , (cboxctr[1]+int(cboxsize[1]/2)))

			cropbox = (cboxtl + cboxbr)
			ccrop = imthresh.crop(cropbox)

			shrunk = 1

		else:
			prescom = ( cboxtl[0]+com[1] , cboxtl[1]+com[0] )	#precise CoM (absolute)
			done = 1

	ccrop = imtrim.crop(cropbox)
	#ccrop.show()
	return prescom

def findangle(spot1, spot2):
	angle = math.degrees(math.atan((abs(spot1[1]-spot2[1]))/(abs(spot1[0]-spot2[0]))))
	return angle

######

desiredspotangle = 49+180	#desired sunspot angle in degrees

def do_sunrot(filename, dir1, dir2):
	global infile
	infile = "img/" + dir1 + "/" + filename
	outfile = "img/" + dir2 + "/" + filename
	try:
		im = Image.open(infile)
		# print "\nFile %s (%s, %s, %d x %d)" % (infile, im.format, im.mode, im.size[0], im.size[1])

		imtrim = im
		immono = ImageOps.equalize(ImageOps.grayscale(imtrim))
		imneg = ImageOps.invert(imtrim)
		global imthresh
		imthresh = imneg.point(sun.thresh1)

		spot1 = findspot( (1075,845), (350,350), (64,64), 10 )
		print "Sunspot 1 is at (%f, %f)" % (spot1[0], spot1[1])
		spot2 = findspot( (845,1105), (350,350), (64,64), 10 )
		print "Sunspot 2 is at (%f, %f)" % (spot2[0], spot2[1])

		spotangle = findangle(spot1,spot2)
		print "Angle between sunspots is %f degs" % spotangle

		print "Rotating..."
		im = imtrim.rotate((desiredspotangle-spotangle), Image.BICUBIC, 0)

		print "Trimming..."
		im = sun.bbcrop(im, 160)

		# print "Saving to %s" % outfile
		im.save(outfile)
	except:
		print "Error occured while processing %s" % (infile)
		f.write("%s\n" % (infile))