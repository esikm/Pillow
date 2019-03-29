.. py:module:: PIL2.ImageFile
.. py:currentmodule:: PIL2.ImageFile

:py:mod:`ImageFile` Module
==========================

The :py:mod:`ImageFile` module provides support functions for the image open
and save functions.

In addition, it provides a :py:class:`Parser` class which can be used to decode
an image piece by piece (e.g. while receiving it over a network connection).
This class implements the same consumer interface as the standard **sgmllib**
and **xmllib** modules.

Example: Parse an image
-----------------------

.. code-block:: python

    from PIL2 import ImageFile

    fp = open("hopper.pgm", "rb")

    p = ImageFile.Parser()

    while 1:
        s = fp.read(1024)
        if not s:
            break
        p.feed(s)

    im = p.close()

    im.save("copy.jpg")


:py:class:`~PIL2.ImageFile.Parser`
---------------------------------

.. autoclass:: PIL2.ImageFile.Parser()
    :members:

:py:class:`~PIL2.ImageFile.PyDecoder`
------------------------------------

.. autoclass:: PIL2.ImageFile.PyDecoder()
    :members:
