.. highlight:: python
.. module:: fontParts.base

######
Anchor
######

********
Overview
********

Anchors are single points in a glyph which are not part of a contour. They can be used as reference positions for doing things like assembling components. In most font editors, anchors have a special appearance and can be edited.

::

	glyph = CurrentGlyph()
	for anchor in glyph.anchors:
	    print anchor


Parents
=======

* :attr:`~BaseAnchor.glyph` The anchor's parent :class:`BaseGlyph`.
* :attr:`~BaseAnchor.layer` The anchor's parent :class:`BaseLayer`.
* :attr:`~BaseAnchor.font`  The anchor's parent :class:`BaseFont`.

Identification
==============

* :attr:`~BaseAnchor.name` The name of the anchor.
* :attr:`~BaseAnchor.color` The color of the anchor.
* :attr:`~BaseAnchor.identifier` The identifier of the anchor.
* :attr:`~BaseAnchor.index` The index of the anchor within the parent glyph's ordered list of anchors.

Coordinate
==========

* :attr:`~BaseAnchor.x` The x position of the anchor.
* :attr:`~BaseAnchor.y` The y position of the anchor.

Copy
====

* :attr:`~BaseAnchor.copy` Copy the anchor.

Transformations
===============

* :attr:`~BaseAnchor.transformBy` Transform the anchor with a transformation matrix.
* :attr:`~BaseAnchor.moveBy` Move the anchor.
* :attr:`~BaseAnchor.scaleBy` Scale the anchor.
* :attr:`~BaseAnchor.rotateBy` Rotate the anchor.
* :attr:`~BaseAnchor.skewBy` Skew the anchor.

Normalization
=============

* :attr:`~BaseAnchor.round` Round the anchor.

Environment
===========

* :attr:`~BaseAnchor.naked` Get the environment's native anchor object.
* :attr:`~BaseAnchor.update` Inform the environment to updat ethe anchor.


*********
Reference
*********

.. autoclass:: BaseAnchor

	.. autoattribute:: color
	.. autoattribute:: font
	.. autoattribute:: glyph
	.. autoattribute:: identifier
	.. autoattribute:: index
	.. autoattribute:: layer
	.. autoattribute:: name
	.. autoattribute:: x
	.. autoattribute:: y

	.. automethod:: copy
	.. automethod:: moveBy
	.. automethod:: naked
	.. automethod:: rotateBy
	.. automethod:: round
	.. automethod:: scaleBy
	.. automethod:: skewBy
	.. automethod:: transformBy
	.. automethod:: update
