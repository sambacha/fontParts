.. highlight:: python
.. module:: fontParts.base

#####
Glyph
#####

.. autoclass:: BaseGlyph

Copy
====

.. automethod:: BaseGlyph.copy

Parents
=======

.. autoattribute:: BaseGlyph.layer
.. autoattribute:: BaseGlyph.font

Identification
==============

.. autoattribute:: BaseGlyph.name
.. autoattribute:: BaseGlyph.unicodes
.. autoattribute:: BaseGlyph.unicode
.. autoattribute:: BaseGlyph.unicode

Metrics
=======

.. autoattribute:: BaseGlyph.width
.. autoattribute:: BaseGlyph.leftMargin
.. autoattribute:: BaseGlyph.rightMargin
.. autoattribute:: BaseGlyph.height
.. autoattribute:: BaseGlyph.bottomMargin
.. autoattribute:: BaseGlyph.topMargin

Queries
=======

.. autoattribute:: BaseGlyph.bounds
.. automethod:: BaseGlyph.pointInside

Pens and Drawing
================

.. automethod:: BaseGlyph.getPen
.. automethod:: BaseGlyph.getPointPen
.. automethod:: BaseGlyph.draw
.. automethod:: BaseGlyph.drawPoints

Layers
======

Layer interaction in glyphs is very similar to the layer interaction in fonts. When you ask a glyph for a layer, you get a *glyph layer* in return. A glyph layer lets you do anything that you can do to a glyph. In fact a glyph layer is really just a glyph.

    >>> bgdGlyph = glyph.newLayer('background')
    >>> bgdGlyph.appendGlyph(glyph)
    >>> bgdGlyph.appendGuideline((10, 10), 45)

.. autoattribute:: BaseGlyph.layers
.. automethod:: BaseGlyph.getLayer
.. automethod:: BaseGlyph.newLayer
.. automethod:: BaseGlyph.removeLayer

Global
======

.. automethod:: BaseGlyph.clear
.. automethod:: BaseGlyph.appendGlyph

Contours
========

.. autoattribute:: BaseGlyph.contours
.. automethod:: BaseGlyph.__len__
.. automethod:: BaseGlyph.__iter__
.. automethod:: BaseGlyph.__getitem__
.. automethod:: BaseGlyph.appendContour
.. automethod:: BaseGlyph.removeContour
.. automethod:: BaseGlyph.clearContours
.. automethod:: BaseGlyph.removeOverlap

Components
==========

.. autoattribute:: BaseGlyph.components
.. automethod:: BaseGlyph.appendComponent
.. automethod:: BaseGlyph.removeComponent
.. automethod:: BaseGlyph.clearComponents
.. automethod:: BaseGlyph.decompose

Anchors
=======

.. autoattribute:: BaseGlyph.anchors
.. automethod:: BaseGlyph.appendAnchor
.. automethod:: BaseGlyph.removeAnchor
.. automethod:: BaseGlyph.clearAnchors

Guidelines
==========

.. autoattribute:: BaseGlyph.guidelines
.. automethod:: BaseGlyph.appendGuideline
.. automethod:: BaseGlyph.removeGuideline
.. automethod:: BaseGlyph.clearGuidelines

Image
=====

.. autoattribute:: BaseGlyph.image
.. automethod:: BaseGlyph.addImage
.. automethod:: BaseGlyph.clearImage

Note
====

.. autoattribute:: BaseGlyph.note
.. autoattribute:: BaseGlyph.markColor

Sub-Objects
===========

.. autoattribute:: BaseGlyph.lib

Transformations
===============

.. automethod:: BaseGlyph.transformBy
.. automethod:: BaseGlyph.moveBy
.. automethod:: BaseGlyph.scaleBy
.. automethod:: BaseGlyph.rotateBy
.. automethod:: BaseGlyph.skewBy

Interpolation
=============

.. automethod:: BaseGlyph.isCompatible
.. automethod:: BaseGlyph.interpolate

Normalization
=============

.. automethod:: BaseGlyph.round
.. automethod:: BaseGlyph.autoUnicodes

Environment
===========

.. automethod:: BaseGlyph.naked
.. automethod:: BaseGlyph.changed
