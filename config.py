#!/usr/bin/env python
# ian.heywood@physics.ox.ac.uk

# sub-image central RA [deg]:
ra0 = 255.705666666667
# sub-image central Dec [deg]
dec0 = -48.7896666666667
# sub-image horizontal extent [deg]
dx = 0.3
# sub-image vertical extent [deg]
dy = 0.17

# executable for Montage mSubimage tool
mSubimage_exec = 'mSubimage'
# executable for Montage mSubimage tool
mViewer_exec = 'mViewer'

# folder containing source FITS files
infolder = '/home/tremou/fits_files/'
# prefix for output FITS files
oplabel = 'GX339-4'
# output folder for subimages
opfolder = 'subims'

# major axis for common convolution (value-unit string)
conv_bmaj = '8.0arcsec'
# minor axis for common convolution (value-unit string)
conv_bmin = '8.0arcsec'
# position angle for common convolution (value-unit string)
conv_bpa = '0.0deg'
# 