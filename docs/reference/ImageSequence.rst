.. py:module:: PIL2.ImageSequence
.. py:currentmodule:: PIL2.ImageSequence

:py:mod:`ImageSequence` Module
==============================

The :py:mod:`ImageSequence` module contains a wrapper class that lets you
iterate over the frames of an image sequence.

Extracting frames from an animation
-----------------------------------

.. code-block:: python

    from PIL2 import Image, ImageSequence

    im = Image.open("animation.fli")

    index = 1
    for frame in ImageSequence.Iterator(im):
        frame.save("frame%d.png" % index)
        index += 1

The :py:class:`~PIL2.ImageSequence.Iterator` class
-------------------------------------------------

.. autoclass:: PIL2.ImageSequence.Iterator
