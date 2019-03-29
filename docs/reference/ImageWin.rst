.. py:module:: PIL2.ImageWin
.. py:currentmodule:: PIL2.ImageWin

:py:mod:`ImageWin` Module (Windows-only)
========================================

The :py:mod:`ImageWin` module contains support to create and display images on
Windows.

ImageWin can be used with PythonWin and other user interface toolkits that
provide access to Windows device contexts or window handles. For example,
Tkinter makes the window handle available via the winfo_id method:

.. code-block:: python

    from PIL2 import ImageWin

    dib = ImageWin.Dib(...)

    hwnd = ImageWin.HWND(widget.winfo_id())
    dib.draw(hwnd, xy)


.. autoclass:: PIL2.ImageWin.Dib
    :members:


.. autoclass:: PIL2.ImageWin.HDC
.. autoclass:: PIL2.ImageWin.HWND
