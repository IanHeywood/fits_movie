# ian.heywood@physics.ox.ac.uk


import glob
import numpy
import os
import sys


execfile('config.py')


CWD = os.getcwd()
opfolder = CWD+'/'+opfolder.rstrip('/')+'/'


fitslist = glob.glob(opfolder.rstrip('/')+'/'+oplabel+'*fits')


for infits in fitslist:

	opimg = infits.replace('.fits','_conv.img')
	opfits = infits.replace('.fits','_conv.fits')

	ia.open(infits)
	ia.convolve2d(outfile=opimg,major=conv_bmaj,minor=conv_bmin,pa=conv_bpa)
	exportfits(imagename=opimg,fitsimage=opfits)
	os.system('rm -rf '+opimg)
	ia.done()