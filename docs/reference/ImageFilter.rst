.. py:module:: PIL2.ImageFilter
.. py:currentmodule:: PIL2.ImageFilter

:py:mod:`ImageFilter` Module
============================

The :py:mod:`ImageFilter` module contains definitions for a pre-defined set of
filters, which can be be used with the :py:meth:`Image.filter()
<PIL2.Image.Image.filter>` method.

Example: Filter an image
------------------------

.. code-block:: python

    from PIL2 import ImageFilter

    im1 = im.filter(ImageFilter.BLUR)

    im2 = im.filter(ImageFilter.MinFilter(3))
    im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)

Filters
-------

The current version of the library provides the following set of predefined
image enhancement filters:

* **BLUR**
* **CONTOUR**
* **DETAIL**
* **EDGE_ENHANCE**
* **EDGE_ENHANCE_MORE**
* **EMBOSS**
* **FIND_EDGES**
* **SHARPEN**
* **SMOOTH**
* **SMOOTH_MORE**

.. autoclass:: PIL2.ImageFilter.Color3DLUT
.. autoclass:: PIL2.ImageFilter.BoxBlur
.. autoclass:: PIL2.ImageFilter.GaussianBlur
.. autoclass:: PIL2.ImageFilter.UnsharpMask
.. autoclass:: PIL2.ImageFilter.Kernel
.. autoclass:: PIL2.ImageFilter.RankFilter
.. autoclass:: PIL2.ImageFilter.MedianFilter
.. autoclass:: PIL2.ImageFilter.MinFilter
.. autoclass:: PIL2.ImageFilter.MaxFilter
.. autoclass:: PIL2.ImageFilter.ModeFilter
