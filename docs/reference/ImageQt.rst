.. py:module:: PIL2.ImageQt
.. py:currentmodule:: PIL2.ImageQt

:py:mod:`ImageQt` Module
========================

The :py:mod:`ImageQt` module contains support for creating PyQt4, PyQt5 or
PySide QImage objects from PIL2 images.

.. versionadded:: 1.1.6

.. py:class:: ImageQt.ImageQt(image)

    Creates an :py:class:`~PIL2.ImageQt.ImageQt` object from a PIL2
    :py:class:`~PIL2.Image.Image` object. This class is a subclass of
    QtGui.QImage, which means that you can pass the resulting objects directly
    to PyQt4/PyQt5/PySide API functions and methods.

    This operation is currently supported for mode 1, L, P, RGB, and RGBA
    images. To handle other modes, you need to convert the image first.
