.. py:module:: PIL2.Image
.. py:currentmodule:: PIL2.Image

:py:mod:`Image` Module
======================

The :py:mod:`~PIL2.Image` module provides a class with the same name which is
used to represent a PIL2 image. The module also provides a number of factory
functions, including functions to load images from files, and to create new
images.

Examples
--------

Open, rotate, and display an image (using the default viewer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script loads an image, rotates it 45 degrees, and displays it
using an external viewer (usually xv on Unix, and the paint program on
Windows).

.. code-block:: python

    from PIL2 import Image
    im = Image.open("bride.jpg")
    im.rotate(45).show()

Create thumbnails
^^^^^^^^^^^^^^^^^

The following script creates nice thumbnails of all JPEG images in the
current directory preserving aspect ratios with 128x128 max resolution.

.. code-block:: python

    from PIL2 import Image
    import glob, os

    size = 128, 128

    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")

Functions
---------

.. autofunction:: open

    .. warning::
        To protect against potential DOS attacks caused by "`decompression bombs`_" (i.e. malicious files
        which decompress into a huge amount of data and are designed to crash or cause disruption by using up
        a lot of memory), Pillow will issue a `DecompressionBombWarning` if the image is over a certain
        limit. If desired, the warning can be turned into an error with
        ``warnings.simplefilter('error', Image.DecompressionBombWarning)`` or suppressed entirely with
        ``warnings.simplefilter('ignore', Image.DecompressionBombWarning)``. See also `the logging
        documentation`_ to have warnings output to the logging facility instead of stderr.

	.. _decompression bombs: https://en.wikipedia.org/wiki/Zip_bomb
	.. _the logging documentation: https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module

Image processing
^^^^^^^^^^^^^^^^

.. autofunction:: alpha_composite
.. autofunction:: blend
.. autofunction:: composite
.. autofunction:: eval
.. autofunction:: merge

Constructing images
^^^^^^^^^^^^^^^^^^^

.. autofunction:: new
.. autofunction:: fromarray
.. autofunction:: frombytes
.. autofunction:: fromstring
.. autofunction:: frombuffer

Registering plugins
^^^^^^^^^^^^^^^^^^^

.. note::

    These functions are for use by plugin authors. Application authors can
    ignore them.

.. autofunction:: register_open
.. autofunction:: register_decoder
.. autofunction:: register_mime
.. autofunction:: register_save
.. autofunction:: register_encoder
.. autofunction:: register_extension


The Image Class
---------------

.. autoclass:: PIL2.Image.Image

An instance of the :py:class:`~PIL2.Image.Image` class has the following
methods. Unless otherwise stated, all methods return a new instance of the
:py:class:`~PIL2.Image.Image` class, holding the resulting image.


.. automethod:: PIL2.Image.Image.alpha_composite
.. automethod:: PIL2.Image.Image.convert

The following example converts an RGB image (linearly calibrated according to
ITU-R 709, using the D65 luminant) to the CIE XYZ color space:

.. code-block:: python

    rgb2xyz = (
        0.412453, 0.357580, 0.180423, 0,
        0.212671, 0.715160, 0.072169, 0,
        0.019334, 0.119193, 0.950227, 0 )
    out = im.convert("RGB", rgb2xyz)

.. automethod:: PIL2.Image.Image.copy
.. automethod:: PIL2.Image.Image.crop
.. automethod:: PIL2.Image.Image.draft
.. automethod:: PIL2.Image.Image.filter
.. automethod:: PIL2.Image.Image.getbands
.. automethod:: PIL2.Image.Image.getbbox
.. automethod:: PIL2.Image.Image.getcolors
.. automethod:: PIL2.Image.Image.getdata
.. automethod:: PIL2.Image.Image.getextrema
.. automethod:: PIL2.Image.Image.getpalette
.. automethod:: PIL2.Image.Image.getpixel
.. automethod:: PIL2.Image.Image.histogram
.. automethod:: PIL2.Image.Image.offset
.. automethod:: PIL2.Image.Image.paste
.. automethod:: PIL2.Image.Image.point
.. automethod:: PIL2.Image.Image.putalpha
.. automethod:: PIL2.Image.Image.putdata
.. automethod:: PIL2.Image.Image.putpalette
.. automethod:: PIL2.Image.Image.putpixel
.. automethod:: PIL2.Image.Image.quantize
.. automethod:: PIL2.Image.Image.resize
.. automethod:: PIL2.Image.Image.remap_palette
.. automethod:: PIL2.Image.Image.rotate
.. automethod:: PIL2.Image.Image.save
.. automethod:: PIL2.Image.Image.seek
.. automethod:: PIL2.Image.Image.show
.. automethod:: PIL2.Image.Image.split
.. automethod:: PIL2.Image.Image.getchannel
.. automethod:: PIL2.Image.Image.tell
.. automethod:: PIL2.Image.Image.thumbnail
.. automethod:: PIL2.Image.Image.tobitmap
.. automethod:: PIL2.Image.Image.tobytes
.. automethod:: PIL2.Image.Image.tostring
.. automethod:: PIL2.Image.Image.transform
.. automethod:: PIL2.Image.Image.transpose
.. automethod:: PIL2.Image.Image.verify

.. automethod:: PIL2.Image.Image.fromstring

.. automethod:: PIL2.Image.Image.load
.. automethod:: PIL2.Image.Image.close

Attributes
----------

Instances of the :py:class:`Image` class have the following attributes:

.. py:attribute:: filename

    The filename or path of the source file. Only images created with the
    factory function `open` have a filename attribute. If the input is a
    file like object, the filename attribute is set to an empty string.

    :type: :py:class: `string`

.. py:attribute:: format

    The file format of the source file. For images created by the library
    itself (via a factory function, or by running a method on an existing
    image), this attribute is set to ``None``.

    :type: :py:class:`string` or ``None``

.. py:attribute:: mode

    Image mode. This is a string specifying the pixel format used by the image.
    Typical values are “1”, “L”, “RGB”, or “CMYK.” See
    :ref:`concept-modes` for a full list.

    :type: :py:class:`string`

.. py:attribute:: size

    Image size, in pixels. The size is given as a 2-tuple (width, height).

    :type: ``(width, height)``

.. py:attribute:: width

    Image width, in pixels.

    :type: :py:class:`int`

.. py:attribute:: height

    Image height, in pixels.

    :type: :py:class:`int`

.. py:attribute:: palette

    Colour palette table, if any. If mode is “P”, this should be an instance of
    the :py:class:`~PIL2.ImagePalette.ImagePalette` class. Otherwise, it should
    be set to ``None``.

    :type: :py:class:`~PIL2.ImagePalette.ImagePalette` or ``None``

.. py:attribute:: info

    A dictionary holding data associated with the image. This dictionary is
    used by file handlers to pass on various non-image information read from
    the file. See documentation for the various file handlers for details.

    Most methods ignore the dictionary when returning new images; since the
    keys are not standardized, it’s not possible for a method to know if the
    operation affects the dictionary. If you need the information later on,
    keep a reference to the info dictionary returned from the open method.

    Unless noted elsewhere, this dictionary does not affect saving files.

    :type: :py:class:`dict`
