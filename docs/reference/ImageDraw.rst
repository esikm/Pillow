.. py:module:: PIL2.ImageDraw
.. py:currentmodule:: PIL2.ImageDraw

:py:mod:`ImageDraw` Module
==========================

The :py:mod:`ImageDraw` module provides simple 2D graphics for
:py:class:`~PIL2.Image.Image` objects.  You can use this module to create new
images, annotate or retouch existing images, and to generate graphics on the
fly for web use.

For a more advanced drawing library for PIL2, see the `aggdraw module`_.

.. _aggdraw module: https://github.com/pytroll/aggdraw

Example: Draw a gray cross over an image
----------------------------------------

.. code-block:: python

    from PIL2 import Image, ImageDraw

    im = Image.open("hopper.jpg")

    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # write to stdout
    im.save(sys.stdout, "PNG")


Concepts
--------

Coordinates
^^^^^^^^^^^

The graphics interface uses the same coordinate system as PIL2 itself, with (0,
0) in the upper left corner.

Colors
^^^^^^

To specify colors, you can use numbers or tuples just as you would use with
:py:meth:`PIL2.Image.new` or :py:meth:`PIL2.Image.Image.putpixel`. For “1”,
“L”, and “I” images, use integers. For “RGB” images, use a 3-tuple containing
integer values. For “F” images, use integer or floating point values.

For palette images (mode “P”), use integers as color indexes. In 1.1.4 and
later, you can also use RGB 3-tuples or color names (see below). The drawing
layer will automatically assign color indexes, as long as you don’t draw with
more than 256 colors.

Color Names
^^^^^^^^^^^

See :ref:`color-names` for the color names supported by Pillow2.

Fonts
^^^^^

PIL2 can use bitmap fonts or OpenType/TrueType fonts.

Bitmap fonts are stored in PIL2’s own format, where each font typically consists
of two files, one named .pil and the other usually named .pbm. The former
contains font metrics, the latter raster data.

To load a bitmap font, use the load functions in the :py:mod:`~PIL2.ImageFont`
module.

To load a OpenType/TrueType font, use the truetype function in the
:py:mod:`~PIL2.ImageFont` module. Note that this function depends on third-party
libraries, and may not available in all PIL2 builds.

Example: Draw Partial Opacity Text
----------------------------------

.. code-block:: python

    from PIL2 import Image, ImageDraw, ImageFont
    # get an image
    base = Image.open('Pillow2/Tests/images/hopper.png').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype('Pillow2/Tests/fonts/FreeMono.ttf', 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
    # draw text, full opacity
    d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

    out = Image.alpha_composite(base, txt)

    out.show()



Functions
---------

.. py:class:: PIL2.ImageDraw.Draw(im, mode=None)

    Creates an object that can be used to draw in the given image.

    Note that the image will be modified in place.

    :param im: The image to draw in.
    :param mode: Optional mode to use for color values.  For RGB
        images, this argument can be RGB or RGBA (to blend the
        drawing into the image).  For all other modes, this argument
        must be the same as the image mode.  If omitted, the mode
        defaults to the mode of the image.

Methods
-------

.. py:method:: PIL2.ImageDraw.ImageDraw.getfont()

    Get the current default font.

    :returns: An image font.

.. py:method:: PIL2.ImageDraw.ImageDraw.arc(xy, start, end, fill=None)

    Draws an arc (a portion of a circle outline) between the start and end
    angles, inside the given bounding box.

    :param xy: Two points to define the bounding box. Sequence of
            ``[(x0, y0), (x1, y1)]`` or ``[x0, y0, x1, y1]``,
             where ``x1 >= x0`` and ``y1 >= y0``.
    :param start: Starting angle, in degrees. Angles are measured from
            3 o'clock, increasing clockwise.
    :param end: Ending angle, in degrees.
    :param fill: Color to use for the arc.

.. py:method:: PIL2.ImageDraw.ImageDraw.bitmap(xy, bitmap, fill=None)

    Draws a bitmap (mask) at the given position, using the current fill color
    for the non-zero portions. The bitmap should be a valid transparency mask
    (mode “1”) or matte (mode “L” or “RGBA”).

    This is equivalent to doing ``image.paste(xy, color, bitmap)``.

    To paste pixel data into an image, use the
    :py:meth:`~PIL2.Image.Image.paste` method on the image itself.

.. py:method:: PIL2.ImageDraw.ImageDraw.chord(xy, start, end, fill=None, outline=None)

    Same as :py:meth:`~PIL2.ImageDraw.ImageDraw.arc`, but connects the end points
    with a straight line.

    :param xy: Two points to define the bounding box. Sequence of
            ``[(x0, y0), (x1, y1)]`` or ``[x0, y0, x1, y1]``,
             where ``x1 >= x0`` and ``y1 >= y0``.
    :param outline: Color to use for the outline.
    :param fill: Color to use for the fill.

.. py:method:: PIL2.ImageDraw.ImageDraw.ellipse(xy, fill=None, outline=None)

    Draws an ellipse inside the given bounding box.

    :param xy: Two points to define the bounding box. Sequence of either
            ``[(x0, y0), (x1, y1)]`` or ``[x0, y0, x1, y1]``,
             where ``x1 >= x0`` and ``y1 >= y0``.
    :param outline: Color to use for the outline.
    :param fill: Color to use for the fill.

.. py:method:: PIL2.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)

    Draws a line between the coordinates in the **xy** list.

    :param xy: Sequence of either 2-tuples like ``[(x, y), (x, y), ...]`` or
               numeric values like ``[x, y, x, y, ...]``.
    :param fill: Color to use for the line.
    :param width: The line width, in pixels.

        .. versionadded:: 1.1.5

        .. note:: This option was broken until version 1.1.6.
    :param joint: Joint type between a sequence of lines. It can be "curve",
                  for rounded edges, or None.

        .. versionadded:: 5.3.0

.. py:method:: PIL2.ImageDraw.ImageDraw.pieslice(xy, start, end, fill=None, outline=None)

    Same as arc, but also draws straight lines between the end points and the
    center of the bounding box.

    :param xy: Two points to define the bounding box. Sequence of
            ``[(x0, y0), (x1, y1)]`` or ``[x0, y0, x1, y1]``,
             where ``x1 >= x0`` and ``y1 >= y0``.
    :param start: Starting angle, in degrees. Angles are measured from
            3 o'clock, increasing clockwise.
    :param end: Ending angle, in degrees.
    :param fill: Color to use for the fill.
    :param outline: Color to use for the outline.

.. py:method:: PIL2.ImageDraw.ImageDraw.point(xy, fill=None)

    Draws points (individual pixels) at the given coordinates.

    :param xy: Sequence of either 2-tuples like ``[(x, y), (x, y), ...]`` or
               numeric values like ``[x, y, x, y, ...]``.
    :param fill: Color to use for the point.

.. py:method:: PIL2.ImageDraw.ImageDraw.polygon(xy, fill=None, outline=None)

    Draws a polygon.

    The polygon outline consists of straight lines between the given
    coordinates, plus a straight line between the last and the first
    coordinate.

    :param xy: Sequence of either 2-tuples like ``[(x, y), (x, y), ...]`` or
               numeric values like ``[x, y, x, y, ...]``.
    :param outline: Color to use for the outline.
    :param fill: Color to use for the fill.

.. py:method:: PIL2.ImageDraw.ImageDraw.rectangle(xy, fill=None, outline=None)

    Draws a rectangle.

    :param xy: Two points to define the bounding box. Sequence of either
            ``[(x0, y0), (x1, y1)]`` or ``[x0, y0, x1, y1]``. The second point
            is just outside the drawn rectangle.
    :param outline: Color to use for the outline.
    :param fill: Color to use for the fill.

.. py:method:: PIL2.ImageDraw.ImageDraw.shape(shape, fill=None, outline=None)

    .. warning:: This method is experimental.

    Draw a shape.

.. py:method:: PIL2.ImageDraw.ImageDraw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left", direction=None, features=None)

    Draws the string at the given position.

    :param xy: Top left corner of the text.
    :param text: Text to be drawn. If it contains any newline characters,
                 the text is passed on to multiline_text()
    :param fill: Color to use for the text.
    :param font: An :py:class:`~PIL2.ImageFont.ImageFont` instance.
    :param spacing: If the text is passed on to multiline_text(),
                    the number of pixels between lines.
    :param align: If the text is passed on to multiline_text(),
                  "left", "center" or "right".
    :param direction: Direction of the text. It can be 'rtl' (right to
                      left), 'ltr' (left to right) or 'ttb' (top to bottom).
                      Requires libraqm.

                      .. versionadded:: 4.2.0

    :param features: A list of OpenType font features to be used during text
                     layout. This is usually used to turn on optional
                     font features that are not enabled by default,
                     for example 'dlig' or 'ss01', but can be also
                     used to turn off default font features for
                     example '-liga' to disable ligatures or '-kern'
                     to disable kerning.  To get all supported
                     features, see
                     https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist
                     Requires libraqm.

                     .. versionadded:: 4.2.0

.. py:method:: PIL2.ImageDraw.ImageDraw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left", direction=None, features=None)

    Draws the string at the given position.

    :param xy: Top left corner of the text.
    :param text: Text to be drawn.
    :param fill: Color to use for the text.
    :param font: An :py:class:`~PIL2.ImageFont.ImageFont` instance.
    :param spacing: The number of pixels between lines.
    :param align: "left", "center" or "right".
    :param direction: Direction of the text. It can be 'rtl' (right to
                      left), 'ltr' (left to right) or 'ttb' (top to bottom).
                      Requires libraqm.

                      .. versionadded:: 4.2.0

    :param features: A list of OpenType font features to be used during text
                     layout. This is usually used to turn on optional
                     font features that are not enabled by default,
                     for example 'dlig' or 'ss01', but can be also
                     used to turn off default font features for
                     example '-liga' to disable ligatures or '-kern'
                     to disable kerning.  To get all supported
                     features, see
                     https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist
                     Requires libraqm.

                     .. versionadded:: 4.2.0

.. py:method:: PIL2.ImageDraw.ImageDraw.textsize(text, font=None, spacing=4, direction=None, features=None)

    Return the size of the given string, in pixels.

    :param text: Text to be measured. If it contains any newline characters,
                 the text is passed on to multiline_textsize()
    :param font: An :py:class:`~PIL2.ImageFont.ImageFont` instance.
    :param spacing: If the text is passed on to multiline_textsize(),
                    the number of pixels between lines.
    :param direction: Direction of the text. It can be 'rtl' (right to
                      left), 'ltr' (left to right) or 'ttb' (top to bottom).
                      Requires libraqm.

                      .. versionadded:: 4.2.0

    :param features: A list of OpenType font features to be used during text
                     layout. This is usually used to turn on optional
                     font features that are not enabled by default,
                     for example 'dlig' or 'ss01', but can be also
                     used to turn off default font features for
                     example '-liga' to disable ligatures or '-kern'
                     to disable kerning.  To get all supported
                     features, see
                     https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist
                     Requires libraqm.

                     .. versionadded:: 4.2.0

.. py:method:: PIL2.ImageDraw.ImageDraw.multiline_textsize(text, font=None, spacing=4, direction=None, features=None)

    Return the size of the given string, in pixels.

    :param text: Text to be measured.
    :param font: An :py:class:`~PIL2.ImageFont.ImageFont` instance.
    :param spacing: The number of pixels between lines.
    :param direction: Direction of the text. It can be 'rtl' (right to
                      left), 'ltr' (left to right) or 'ttb' (top to bottom).
                      Requires libraqm.

                      .. versionadded:: 4.2.0

    :param features: A list of OpenType font features to be used during text
                     layout. This is usually used to turn on optional
                     font features that are not enabled by default,
                     for example 'dlig' or 'ss01', but can be also
                     used to turn off default font features for
                     example '-liga' to disable ligatures or '-kern'
                     to disable kerning.  To get all supported
                     features, see
                     https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist
                     Requires libraqm.

                     .. versionadded:: 4.2.0

.. py:method:: PIL2.ImageDraw.getdraw(im=None, hints=None)

    .. warning:: This method is experimental.

    A more advanced 2D drawing interface for PIL2 images,
    based on the WCK interface.

    :param im: The image to draw in.
    :param hints: An optional list of hints.
    :returns: A (drawing context, drawing resource factory) tuple.

.. py:method:: PIL2.ImageDraw.floodfill(image, xy, value, border=None, thresh=0)

    .. warning:: This method is experimental.

    Fills a bounded region with a given color.

    :param image: Target image.
    :param xy: Seed position (a 2-item coordinate tuple).
    :param value: Fill color.
    :param border: Optional border value.  If given, the region consists of
        pixels with a color different from the border color.  If not given,
        the region consists of pixels having the same color as the seed
        pixel.
    :param thresh: Optional threshold value which specifies a maximum
        tolerable difference of a pixel value from the 'background' in
        order for it to be replaced. Useful for filling regions of non-
        homogeneous, but similar, colors.
