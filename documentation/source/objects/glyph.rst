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
* :meth:`~BaseGlyph.copy` (add general description)

Parents
=======
* :attr:`~BaseGlyph.layer` (add general description)
* :attr:`~BaseGlyph.font` (add general description)

Identification
==============
* :attr:`~BaseGlyph.name` (add general description)
* :attr:`~BaseGlyph.unicodes` (add general description)
* :attr:`~BaseGlyph.unicode` (add general description)
* :meth:`~BaseGlyph.autoUnicodes` (add general description)

Metrics
=======
* :attr:`~BaseGlyph.width` (add general description)
* :attr:`~BaseGlyph.leftMargin` (add general description)
* :attr:`~BaseGlyph.rightMargin` (add general description)
* :attr:`~BaseGlyph.height` (add general description)
* :attr:`~BaseGlyph.bottomMargin` (add general description)
* :attr:`~BaseGlyph.topMargin` (add general description)

Queries
=======
* :attr:`~BaseGlyph.bounds` (add general description)
* :meth:`~BaseGlyph.pointInside` (add general description)

Pens and Drawing
================
* :meth:`~BaseGlyph.getPen` (add general description)
* :meth:`~BaseGlyph.getPointPen` (add general description)
* :meth:`~BaseGlyph.draw` (add general description)
* :meth:`~BaseGlyph.drawPoints` (add general description)

Layers
======
Layer interaction in glyphs is very similar to the layer interaction in fonts. When you ask a glyph for a layer, you get a =glyph layer= in return. A glyph layer lets you do anything that you can do to a glyph. In fact a glyph layer is really just a glyph.

	>>> bgdGlyph = glyph.newLayer(=background=)
	>>> bgdGlyph.appendGlyph(glyph)
	>>> bgdGlyph.appendGuideline((10, 10), 45)

* :attr:`~BaseGlyph.layers` (add general description)
* :meth:`~BaseGlyph.getLayer` (add general description)
* :meth:`~BaseGlyph.newLayer` (add general description)
* :meth:`~BaseGlyph.removeLayer` (add general description)

Global
======
* :meth:`~BaseGlyph.clear` (add general description)
* :meth:`~BaseGlyph.appendGlyph` (add general description)

Contours
========
* :attr:`~BaseGlyph.contours` (add general description)
* :meth:`~BaseGlyph.__len__` (add general description)
* :meth:`~BaseGlyph.__iter__` (add general description)
* :meth:`~BaseGlyph.__getitem__` (add general description)
* :meth:`~BaseGlyph.appendContour` (add general description)
* :meth:`~BaseGlyph.removeContour` (add general description)
* :meth:`~BaseGlyph.clearContours` (add general description)
* :meth:`~BaseGlyph.removeOverlap` (add general description)

Components
==========
* :attr:`~BaseGlyph.components` (add general description)
* :meth:`~BaseGlyph.appendComponent` (add general description)
* :meth:`~BaseGlyph.removeComponent` (add general description)
* :meth:`~BaseGlyph.clearComponents` (add general description)
* :meth:`~BaseGlyph.decompose` (add general description)

Anchors
=======
* :attr:`~BaseGlyph.anchors` (add general description)
* :meth:`~BaseGlyph.appendAnchor` (add general description)
* :meth:`~BaseGlyph.removeAnchor` (add general description)
* :meth:`~BaseGlyph.clearAnchors` (add general description)

Guidelines
==========
* :attr:`~BaseGlyph.guidelines` (add general description)
* :meth:`~BaseGlyph.appendGuideline` (add general description)
* :meth:`~BaseGlyph.removeGuideline` (add general description)
* :meth:`~BaseGlyph.clearGuidelines` (add general description)

Image
=====
* :attr:`~BaseGlyph.image` (add general description)
* :meth:`~BaseGlyph.addImage` (add general description)
* :meth:`~BaseGlyph.clearImage` (add general description)

Note
====
* :attr:`~BaseGlyph.note` (add general description)
* :attr:`~BaseGlyph.markColor` (add general description)

Sub-Objects
===========
* :attr:`~BaseGlyph.lib` (add general description)

Transformations
===============
* :meth:`~BaseGlyph.transformBy` (add general description)
* :meth:`~BaseGlyph.moveBy` (add general description)
* :meth:`~BaseGlyph.scaleBy` (add general description)
* :meth:`~BaseGlyph.rotateBy` (add general description)
* :meth:`~BaseGlyph.skewBy` (add general description)

Interpolation
=============
* :meth:`~BaseGlyph.isCompatible` (add general description)
* :meth:`~BaseGlyph.interpolate` (add general description)


Normalization
=============
* :meth:`~BaseGlyph.round` (add general description)
* :meth:`~BaseGlyph.autoUnicodes` (add general description)

Environment
===========
* :meth:`~BaseGlyph.naked` (add general description)
* :meth:`~BaseGlyph.changed` (add general description)

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