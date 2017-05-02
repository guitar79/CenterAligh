import os
import sun, suncrop, sunrot, sunscale

directories = ['crop', 'rot', 'scale', 'result']

def make_directories():
	for dirname in directories:
		if not os.path.exists("img/" + dirname):
			os.makedirs("img/" + dirname)

make_directories()

image_extension = ['.JPG', '.jpg']
input_image_list = os.listdir('img/in/')

for filename in input_image_list:
	if(filename[-4:] not in image_extension): # skip file if it's not image file
		continue

	print "File %s" % filename
	suncrop.do_suncrop(filename, 'in', 'crop')
	# sunrot.do_sunrot(filename, 'crop', rot')
	# sunscale.do_sunscale(filename, 'rot', 'result')
	sunscale.do_sunscale(filename, 'crop', 'result')



