.. highlight:: python
.. module:: fontParts.base

######
Anchor
######

Anchors are single points in a glyph which are not part of a contour. They can be used as reference positions for doing things like assembling components. In most font editors, anchors have a special appearance and can be edited.

::

	glyph = CurrentGlyph()
	for anchor in glyph.anchors:
	    print anchor

.. autoclass:: BaseAnchor

Copy
====

.. automethod:: BaseAnchor.copy

Parents
=======

.. autoattribute:: BaseAnchor.glyph
.. autoattribute:: BaseAnchor.layer
.. autoattribute:: BaseAnchor.font

Identification
==============

.. autoattribute:: BaseAnchor.name
.. autoattribute:: BaseAnchor.color
.. autoattribute:: BaseAnchor.identifier
.. autoattribute:: BaseAnchor.index

Coordinate
==========

.. autoattribute:: BaseAnchor.x
.. autoattribute:: BaseAnchor.y

Transformations
===============

.. automethod:: BaseAnchor.transformBy
.. automethod:: BaseAnchor.moveBy
.. automethod:: BaseAnchor.scaleBy
.. automethod:: BaseAnchor.rotateBy
.. automethod:: BaseAnchor.skewBy

Normalization
=============

.. automethod:: BaseAnchor.round

Environment
===========

.. automethod:: BaseAnchor.naked
.. automethod:: BaseAnchor.changed

