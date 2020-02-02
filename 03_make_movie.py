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


	for infits in fitslist:
		oppng = infits.replace('.fits','.png')

		syscall = mViewer_exec+' '
		syscall += '-ct '+str(cmap)+' '
		syscall += '-gray '+infits+' '
		syscall += str(minpix)+' '
		syscall += str(maxpix)+' '
		syscall += '-out '+oppng

		os.system(syscall)

