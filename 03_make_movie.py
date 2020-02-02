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
	fontsize = cfg.fontsize
	delay = cfg.delay


	CWD = os.getcwd()
	opfolder = CWD+'/'+opfolder.rstrip('/')+'/'


	fitslist = sorted(glob.glob(opfolder.rstrip('/')+'/*conv.fits'))

	print opfolder
	print fitslist

	for infits in fitslist:

		oppng = infits.replace('conv.fits','conv.png')
		oppng_label = infits.replace('conv.fits','conv_stamp.png')

		final_gif = oplabel+'_anim.gif'
		final_gif_labels = oplabel+'_dated_anim.gif'

		mjd = infits.split('_')[-2].split('.')[0].replace('p','.')
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
		syscall += '-gravity south -pointsize '+str(fontsize)+' '
		syscall += "-stroke '#000C' -strokewidth 2 "
		syscall += '-annotate 0 '+date+' '
		syscall += '-stroke none -fill white '
		syscall += '-annotate 0 '+date+' '
		syscall += oppng_label

		os.system(syscall)

	syscall = 'convert-im6 '
	syscall += '-loop 0 '
	syscall += '-delay '+str(cfg.delay)+' '
	syscall += opfolder+'*conv.png '
	syscall += final_gif

	os.system(syscall)

	syscall = 'convert-im6 '
	syscall += '-loop 0 '
	syscall += '-delay '+str(cfg.delay)+' '
	syscall += opfolder+'*conv_stamp.png '
	syscall += final_gif_labels

	os.system(syscall)

if __name__ == "__main__":

    main()