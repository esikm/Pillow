.. py:module:: PIL2.ImageChops
.. py:currentmodule:: PIL2.ImageChops

:py:mod:`ImageChops` ("Channel Operations") Module
==================================================

The :py:mod:`ImageChops` module contains a number of arithmetical image
operations, called channel operations (“chops”). These can be used for various
purposes, including special effects, image compositions, algorithmic painting,
and more.

For more pre-made operations, see :py:mod:`ImageOps`.

At this time, most channel operations are only implemented for 8-bit images
(e.g. “L” and “RGB”).

Functions
---------

Most channel operations take one or two image arguments and returns a new
image. Unless otherwise noted, the result of a channel operation is always
clipped to the range 0 to MAX (which is 255 for all modes supported by the
operations in this module).

.. autofunction:: PIL2.ImageChops.add
.. autofunction:: PIL2.ImageChops.add_modulo
.. autofunction:: PIL2.ImageChops.blend
.. autofunction:: PIL2.ImageChops.composite
.. autofunction:: PIL2.ImageChops.constant
.. autofunction:: PIL2.ImageChops.darker
.. autofunction:: PIL2.ImageChops.difference
.. autofunction:: PIL2.ImageChops.duplicate
.. autofunction:: PIL2.ImageChops.invert
.. autofunction:: PIL2.ImageChops.lighter
.. autofunction:: PIL2.ImageChops.logical_and
.. autofunction:: PIL2.ImageChops.logical_or
.. autofunction:: PIL2.ImageChops.multiply
.. py:method:: PIL2.ImageChops.offset(image, xoffset, yoffset=None)

    Returns a copy of the image where data has been offset by the given
    distances. Data wraps around the edges. If **yoffset** is omitted, it
    is assumed to be equal to **xoffset**.

.. autofunction:: PIL2.ImageChops.screen
.. autofunction:: PIL2.ImageChops.subtract
.. autofunction:: PIL2.ImageChops.subtract_modulo
