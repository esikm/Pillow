"""Pillow (Fork of the Python Imaging Library)

Pillow is the friendly PIL2 fork by Alex Clark and Contributors.
    https://github.com/python-pillow/Pillow/

Pillow is forked from PIL2 1.1.7.

PIL2 is the Python Imaging Library by Fredrik Lundh and Contributors.
Copyright (c) 1999 by Secret Labs AB.

Use PIL2.__version__ for this Pillow version.
PIL2.VERSION is the old PIL2 version and will be removed in the future.

;-)
"""

from . import _version

# VERSION is deprecated and will be removed in Pillow 6.0.0.
# PILLOW_VERSION is deprecated and will be removed after that.
# Use __version__ instead.
VERSION = '1.1.7'  # PIL2 Version
PILLOW_VERSION = __version__ = _version.__version__

del _version


_plugins = ['BlpImagePlugin',
            'BmpImagePlugin',
            'BufrStubImagePlugin',
            'CurImagePlugin',
            'DcxImagePlugin',
            'DdsImagePlugin',
            'EpsImagePlugin',
            'FitsStubImagePlugin',
            'FliImagePlugin',
            'FpxImagePlugin',
            'FtexImagePlugin',
            'GbrImagePlugin',
            'GifImagePlugin',
            'GribStubImagePlugin',
            'Hdf5StubImagePlugin',
            'IcnsImagePlugin',
            'IcoImagePlugin',
            'ImImagePlugin',
            'ImtImagePlugin',
            'IptcImagePlugin',
            'JpegImagePlugin',
            'Jpeg2KImagePlugin',
            'McIdasImagePlugin',
            'MicImagePlugin',
            'MpegImagePlugin',
            'MpoImagePlugin',
            'MspImagePlugin',
            'PalmImagePlugin',
            'PcdImagePlugin',
            'PcxImagePlugin',
            'PdfImagePlugin',
            'PixarImagePlugin',
            'PngImagePlugin',
            'PpmImagePlugin',
            'PsdImagePlugin',
            'SgiImagePlugin',
            'SpiderImagePlugin',
            'SunImagePlugin',
            'TgaImagePlugin',
            'TiffImagePlugin',
            'WebPImagePlugin',
            'WmfImagePlugin',
            'XbmImagePlugin',
            'XpmImagePlugin',
            'XVThumbImagePlugin']
