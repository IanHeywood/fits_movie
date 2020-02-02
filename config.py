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
# executable for ImageMagick convert-im6
convert_exec = 'convert-im6'

# folder containing source FITS files
infolder = '/home/tremou/fits_files/'
# prefix for output FITS files
oplabel = 'GX339-4'
# output folder for subimages
opfolder = 'subims'

# major axis for common convolution (value-unit string)
conv_bmaj = '10.0arcsec'
# minor axis for common convolution (value-unit string)
conv_bmin = '10.0arcsec'
# position angle for common convolution (value-unit string)
conv_bpa = '0.0deg'

# pixel minimum for frames
minpix = -1e-4
# pixel minimum for frames
maxpix = 1e-3
# colour map (see http://montage.ipac.caltech.edu/mViewer/mViewer_grayscale.html)
cmap = 1
# font size for date labels
fontsize = 24
# frame delay for GIFs 
delay = 10