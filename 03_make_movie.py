#!/usr/bin/env python
# ian.heywood@physics.ox.ac.uk


import config as cfg
import glob
import os
from astropy.time import Time


def main():


	opfolder = cfg.opfolder
	oplabel = cfg.oplabel
	mViewer_exec = cfg.mViewer_exec
	convert_exec = cfg.convert_exec
	minpix = cfg.minpix
	maxpix = cfg.maxpix
	cmap = cfg.cmap


	CWD = os.getcwd()
	opfolder = CWD+'/'+opfolder.rstrip('/')+'/'


	fitslist = sorted(glob.glob(opfolder.rstrip('/')+'/*conv.fits'))

	print opfolder
	print fitslist

	for infits in fitslist:

		oppng = infits.replace('.fits','.png')
		oppng_label = infits.replace('.fits','_stamp.png')
		mjd = infits.split('_')[-1].split('.')[0].replace('p','.')
		t = Time(float(mjd), format='mjd', scale='utc')
		date = t.iso.split(' ')[0]

		syscall = mViewer_exec+' '
		syscall += '-ct '+str(cmap)+' '
		syscall += '-gray '+infits+' '
		syscall += str(minpix)+' '
		syscall += str(maxpix)+' '
		syscall += '-out '+oppng

		os.system(syscall)

		syscall = 'convert-im6 '+oppng+' '
		syscall += "-stroke '#000C' -strokewidth 2 "
		syscall += '-annotate 0 '+date+' '
		syscall += '-stroke none -fill white '
		syscall += '-annotate 0 '+date+' '
		syscall += oppng_label

		os.system(syscall)



if __name__ == "__main__":

    main()