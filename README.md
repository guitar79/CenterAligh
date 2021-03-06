# CenterAlign

Sun eclipse image aligning tool, a fork of [Aligning sun images using python](https://labjg.wordpress.com/2013/04/01/aligning-sun-images-using-python/).

## Instructions

- Create `img` directory.
- Create `in` in `img` directory.
- Place your sun files at `img/in/`.
- Run `python2 run.py`.

## Results

- Processed images are saved to `img/result/`.
- List of images that made an error are saved to `errorlog.txt`.

## Download Smaple eclipse images from my NAS
2009. 7. 22. : http://parksparks.iptime.org:500/fbsharing/Ht8sDf94
2010. 1. 15. : http://parksparks.iptime.org:500/fbsharing/jTZXUCib
 
## Mechanism

1. `run.py` = (Find image files) + `do_suncrop` + `do_sunrot`.
1. `do_suncrop` @ `suncrop.py` : Finds the center of Sun and crops it around.
1. `do_sunrot` @ `sunrot.py` : (NOT USED) Rotates the image to align Sun's angle. This requires more than two sunspots on Sun.
1. `do_sunscale` @ `sunscale.py` : (WIP) Adjusts the Sun's size on image.
