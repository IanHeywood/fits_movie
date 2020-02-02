# fits_movie

These scripts will turn a folder full of FITS images into an animated GIF movie. The input images must have a `DATE-OBS` keyword in the header, as this is used to ensure the correct running order.

The scripts rely on [Montage](http://montage.ipac.caltech.edu/) (for cropping and rendering PNGs), [CASA](http://casa.nrao.edu) (for 2D convolution), and [ImageMagick](https://imagemagick.org/index.php) (for annotation and rendering an animated GIF).

If the exectuables are in non-standard locations then they can be specified in the [config.py](https://github.com/IanHeywood/fits_movie/blob/master/config.py) script, which also controls all the other parameters, including the path to the source images.

### Usage

Make a working folder:

```
$ mkdir my_movie
$ cd my_movie
```

Clone this repo:

```
$ git clone https://github.com/IanHeywood/fits_movie.git .
```

Edit `config.py` to suit your needs, then just run everything in sequence:

```
$ python 01_ordered_subimages.py
$ casa -c 02_casa_convolve.py
$ python 03_make_movie.py
```

After which you should have a pair of animated GIFs in your working folder, one with timestamps (nearest day only, at present) and one without.
