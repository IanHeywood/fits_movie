from astropy.time import Time
from astropy.io import fits
import os
import sys
import glob
import config as cfg


def get_map_date(infits):
	input_hdu = fits.open(infits)[0]
	hdr = input_hdu.header
	return hdr.get('DATE-OBS')




def main():


	ra0 = cfg.ra0
	dec0 = cfg.dec0	
	dx = cfg.dx
	dy = cfg.dy
	infolder = cfg.infolder
	opfolder = cfg.opfolder
	oplabel = cfg.oplabel
	mSubimage_exec = cfg.mSubimage_exec


	# ra0 = 255.705666666667
	# dec0 = -48.7896666666667
	# dx = 0.3
	# dy = 0.17
	# infolder = '/home/tremou/fits_files/'
	# opfolder = 'subims'
	# oplabel = 'GX339-4'
	# mSubimage_exec = 'mSubimage'


	CWD = os.getcwd()
	opfolder = CWD+'/'+opfolder.rstrip('/')+'/'
	if not os.path.isdir(opfolder):
		os.mkdir(opfolder)

	fitslist = glob.glob(infolder.rstrip('/')+'/*fits')


	for infits in fitslist:

		map_date = get_map_date(infits)

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


if __name__ == "__main__":

    main()
