.. py:module:: PIL2.ImageStat
.. py:currentmodule:: PIL2.ImageStat

:py:mod:`ImageStat` Module
==========================

The :py:mod:`ImageStat` module calculates global statistics for an image, or
for a region of an image.

.. py:class:: PIL2.ImageStat.Stat(image_or_list, mask=None)

    Calculate statistics for the given image. If a mask is included,
    only the regions covered by that mask are included in the
    statistics. You can also pass in a previously calculated histogram.

    :param image: A PIL2 image, or a precalculated histogram.
    :param mask: An optional mask.

    .. py:attribute:: extrema

        Min/max values for each band in the image.

    .. py:attribute:: count

        Total number of pixels for each band in the image.

    .. py:attribute:: sum

        Sum of all pixels for each band in the image.

    .. py:attribute:: sum2

        Squared sum of all pixels for each band in the image.

    .. py:attribute:: mean

        Average (arithmetic mean) pixel level for each band in the image.

    .. py:attribute:: median

        Median pixel level for each band in the image.

    .. py:attribute:: rms

        RMS (root-mean-square) for each band in the image.

    .. py:attribute:: var

        Variance for each band in the image.

    .. py:attribute:: stddev

        Standard deviation for each band in the image.
