import config as cfg
import glob
import numpy
import os
import sys
from astropy.time import Time
from astropy.io import fits


def get_map_info(infits):
	input_hdu = fits.open(infits)[0]
	hdr = input_hdu.header
	map_date = hdr.get('DATE-OBS')
	bmaj = hdr.get('BMAJ')*3600.0
	bmin = hdr.get('BMIN')*3600.0
	bpa = hdr.get('BPA')
	return map_date,bmaj,bmin,bpa


def main():


	ra0 = cfg.ra0
	dec0 = cfg.dec0	
	dx = cfg.dx
	dy = cfg.dy
	infolder = cfg.infolder
	opfolder = cfg.opfolder
	oplabel = cfg.oplabel
	mSubimage_exec = cfg.mSubimage_exec

	CWD = os.getcwd()
	opfolder = CWD+'/'+opfolder.rstrip('/')+'/'


	if not os.path.isdir(opfolder):
		os.mkdir(opfolder)


	fitslist = glob.glob(infolder.rstrip('/')+'/*fits')


	bmajs = []
	bmins = []
	bpas = []


	for infits in fitslist:

		map_date,bmaj,bmin,bpa = get_map_info(infits)

		bmajs.append(bmaj)
		bmins.append(bmin)
		bpas.append(bpa)

		if map_date:

			t = Time(map_date, format='isot', scale='utc')
			tmjd = str(t.mjd).replace('.','p')
			opfits = oplabel+'_'+tmjd+'.fits'

			print opfolder+opfits

			if os.path.isfile(opfolder+opfits):

				print opfits+'exists, skipping'

			else:

				syscall = mSubimage_exec+' '
				syscall += infits+' '
				syscall += opfolder+opfits+' '
				syscall += str(ra0)+' '+str(dec0)+' '
				syscall += str(dx)+' '+str(dy)

				os.system(syscall)

	bmajs = numpy.array(bmajs)
	bmins = numpy.array(bmins)
	bpas = numpy.array(bpas)


	print('')
	print('Restoring beam properties from input images:')
	print('')
	print('Median / std major axis [asec]: ',numpy.median(bpas),numpy.std(bpas))
	print('Median / std minor axis [asec]: ',numpy.median(bpas),numpy.std(bpas))
	print('Median / std PA [deg]         : ',numpy.median(bpas),numpy.std(bpas))


if __name__ == "__main__":

    main()
