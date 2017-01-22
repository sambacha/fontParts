.. highlight:: python
.. module:: fontParts.base

#####
Glyph
#####

********
Overview
********

.. class:: BaseGlyph

Copy
====

* :meth:`~BaseGlyph.copy` Copy the glyph.

Parents
=======

* :attr:`~BaseGlyph.layer` The glyph's parent :class:`BaseLayer`.
* :attr:`~BaseGlyph.font` The glyph's parent :class:`BaseFont`.

Identification
==============

* :attr:`~BaseGlyph.name` The glyph name.
* :attr:`~BaseGlyph.unicodes` A list of unicode values for this glyph.

	.. note:: Not all applications and editors support multiple unicode values for a glyph. Assume that ``glyph.unicode == glyph.unicodes[0]``.

* :attr:`~BaseGlyph.unicode` The unicode value for this glyph, integer.
* :meth:`~BaseGlyph.autoUnicodes` Try to find unicode values for this glyph.

Metrics
=======

* :attr:`~BaseGlyph.width` The horizontal advance width of the glyph.
* :attr:`~BaseGlyph.leftMargin` The left margin of the glyph.
* :attr:`~BaseGlyph.rightMargin` The right margin of the glyph.
* :attr:`~BaseGlyph.height` The vertical advance width of the glyph.
* :attr:`~BaseGlyph.bottomMargin` The bottom margin of the glyph.
* :attr:`~BaseGlyph.topMargin` The top margin of the glyph.

Queries
=======

* :attr:`~BaseGlyph.bounds` The bounding box. The values are ``(xMin, yMin, xMax, yMax)``, or ``None`` if the glyph has no contours.
* :meth:`~BaseGlyph.pointInside` Returns ``True`` if the point is inside the "black" area of the glyph or ``False`` if the point is inside the "white" area of the glyph.

Pens and Drawing
================

* :meth:`~BaseGlyph.getPen` Returns an appropriate Pen object to draw in this glyph.
* :meth:`~BaseGlyph.getPointPen` Returns an appropriate PointPen object to draw in this glyph.
* :meth:`~BaseGlyph.draw` Get this glyph to draw itself with the pen on offer.
* :meth:`~BaseGlyph.drawPoints` Get this glyph to draw itself with the points pen on offer.

Layers
======

Layer interaction in glyphs is very similar to the layer interaction in fonts. When you ask a glyph for a layer, you get a *glyph layer* in return. A glyph layer lets you do anything that you can do to a glyph. In fact a glyph layer is really just a glyph.

	>>> bgdGlyph = glyph.newLayer('background')
	>>> bgdGlyph.appendGlyph(glyph)
	>>> bgdGlyph.appendGuideline((10, 10), 45)

* :attr:`~BaseGlyph.layers` The glyph's :class:`BaseLayer` objects.
* :meth:`~BaseGlyph.getLayer` Get a particular layer from the glyph.
* :meth:`~BaseGlyph.newLayer` Create a layer in the glyph.
* :meth:`~BaseGlyph.removeLayer` Remove a layer from the glyph.

Global
======

* :meth:`~BaseGlyph.clear` (add general description)
* :meth:`~BaseGlyph.appendGlyph` (add general description)

Contours
========

* :attr:`~BaseGlyph.contours` The glyph's :class:`BaseContour` objects.
* :meth:`~BaseGlyph.__len__` The number of contours in the glyph.
* :meth:`~BaseGlyph.__iter__` Iterate over all :class:`BaseContour` objects in the glyph.
* :meth:`~BaseGlyph.__getitem__` Get a particular contour from the glyph.
* :meth:`~BaseGlyph.appendContour` Add a contour to the glyph.
* :meth:`~BaseGlyph.removeContour` Remove a contour from the glyph.
* :meth:`~BaseGlyph.clearContours` Clear all contours in the glyph.
* :meth:`~BaseGlyph.removeOverlap` Remove overlaps in the glyph.

Components
==========

* :attr:`~BaseGlyph.components` The glyph's :class:`BaseComponent` objects.
* :meth:`~BaseGlyph.appendComponent` Add a component to the glyph.
* :meth:`~BaseGlyph.removeComponent` Remove a component from the glyph.
* :meth:`~BaseGlyph.clearComponents` Clear all components in the glyph.
* :meth:`~BaseGlyph.decompose` Replace all component objects with their actual contours.

Anchors
=======

* :attr:`~BaseGlyph.anchors` The glyph's :class:`BaseAnchor` objects.
* :meth:`~BaseGlyph.appendAnchor` Add an anchor to the glyph.
* :meth:`~BaseGlyph.removeAnchor` Remove an anchor from the glyph.
* :meth:`~BaseGlyph.clearAnchors` Clear all anchors in the glyph.

Guidelines
==========

* :attr:`~BaseGlyph.guidelines` The glyph's :class:`BaseGuideline` objects.
* :meth:`~BaseGlyph.appendGuideline` Add a guideline to the glyph.
* :meth:`~BaseGlyph.removeGuideline` Remove an guideline from the glyph.
* :meth:`~BaseGlyph.clearGuidelines` Clear all guidelines in the glyph.

Image
=====

* :attr:`~BaseGlyph.image` The glyph's :class:`BaseImage` object.
* :meth:`~BaseGlyph.addImage` Add an image to the glyph.
* :meth:`~BaseGlyph.clearImage` Clear the image in the glyph.

Note
====

* :attr:`~BaseGlyph.note` A place for a short string, a note about this glyph.
* :attr:`~BaseGlyph.markColor` The mark color for this glyph.

Sub-Objects
===========

* :attr:`~BaseGlyph.lib` The glyph's :class:`BaseLib` object.

Transformations
===============

* :meth:`~BaseGlyph.transformBy` Transform the glyph with a transformation matrix.
* :meth:`~BaseGlyph.moveBy` Move the glyph.
* :meth:`~BaseGlyph.scaleBy` Scale the glyph.
* :meth:`~BaseGlyph.rotateBy` Rotate the glyph.
* :meth:`~BaseGlyph.skewBy` Skew the glyph.

Interpolation
=============

* :meth:`~BaseGlyph.isCompatible` Determine if one glyph is compatible for interpolation with another.
* :meth:`~BaseGlyph.interpolate` Interpolate this font between two other glyphs.

Normalization
=============

* :meth:`~BaseGlyph.round` Round coordinates in the glyph.
* :meth:`~BaseGlyph.autoUnicodes` Try to find unicode values for this glyph.

Environment
===========

* :meth:`~BaseGlyph.naked` Get the environment's native glyph object.
* :meth:`~BaseGlyph.changed` Inform the environment to update the glyph.


*********
Reference
*********

.. autoclass:: BaseGlyph

	.. autoattribute:: BaseGlyph.anchors
	.. autoattribute:: BaseGlyph.bottomMargin
	.. autoattribute:: BaseGlyph.bounds
	.. autoattribute:: BaseGlyph.components
	.. autoattribute:: BaseGlyph.contours
	.. autoattribute:: BaseGlyph.font
	.. autoattribute:: BaseGlyph.guidelines
	.. autoattribute:: BaseGlyph.height
	.. autoattribute:: BaseGlyph.image
	.. autoattribute:: BaseGlyph.layer
	.. autoattribute:: BaseGlyph.layers
	.. autoattribute:: BaseGlyph.leftMargin
	.. autoattribute:: BaseGlyph.lib
	.. autoattribute:: BaseGlyph.markColor
	.. autoattribute:: BaseGlyph.name
	.. autoattribute:: BaseGlyph.note
	.. autoattribute:: BaseGlyph.rightMargin
	.. autoattribute:: BaseGlyph.topMargin
	.. autoattribute:: BaseGlyph.unicode
	.. autoattribute:: BaseGlyph.unicodes
	.. autoattribute:: BaseGlyph.width
	.. automethod:: BaseGlyph.__getitem__
	.. automethod:: BaseGlyph.__iter__
	.. automethod:: BaseGlyph.__len__
	.. automethod:: BaseGlyph.addImage
	.. automethod:: BaseGlyph.appendAnchor
	.. automethod:: BaseGlyph.appendComponent
	.. automethod:: BaseGlyph.appendContour
	.. automethod:: BaseGlyph.appendGlyph
	.. automethod:: BaseGlyph.appendGuideline
	.. automethod:: BaseGlyph.autoUnicodes
	.. automethod:: BaseGlyph.clear
	.. automethod:: BaseGlyph.clearAnchors
	.. automethod:: BaseGlyph.clearComponents
	.. automethod:: BaseGlyph.clearContours
	.. automethod:: BaseGlyph.clearGuidelines
	.. automethod:: BaseGlyph.clearImage
	.. automethod:: BaseGlyph.copy
	.. automethod:: BaseGlyph.decompose
	.. automethod:: BaseGlyph.draw
	.. automethod:: BaseGlyph.drawPoints
	.. automethod:: BaseGlyph.getLayer
	.. automethod:: BaseGlyph.getPen
	.. automethod:: BaseGlyph.getPointPen
	.. automethod:: BaseGlyph.interpolate
	.. automethod:: BaseGlyph.isCompatible
	.. automethod:: BaseGlyph.moveBy
	.. automethod:: BaseGlyph.naked
	.. automethod:: BaseGlyph.newLayer
	.. automethod:: BaseGlyph.pointInside
	.. automethod:: BaseGlyph.removeAnchor
	.. automethod:: BaseGlyph.removeComponent
	.. automethod:: BaseGlyph.removeContour
	.. automethod:: BaseGlyph.removeGuideline
	.. automethod:: BaseGlyph.removeLayer
	.. automethod:: BaseGlyph.removeOverlap
	.. automethod:: BaseGlyph.rotateBy
	.. automethod:: BaseGlyph.round
	.. automethod:: BaseGlyph.scaleBy
	.. automethod:: BaseGlyph.skewBy
	.. automethod:: BaseGlyph.transformBy
	.. automethod:: BaseGlyph.changed
