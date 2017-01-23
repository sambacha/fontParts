.. highlight:: python
.. module:: fontParts.base

#####
Point
#####

Points are single points in a contour. These can be on-curve or off-curve and they have various possible attributes.

::

	glyph = CurrentGlyph()
	for contour in glyph:
		for point in contour.points:
			print point

Copy
====

.. automethod:: BasePoint.copy

Parents
=======

.. autoattribute:: BasePoint.contour
.. autoattribute:: BasePoint.glyph
.. autoattribute:: BasePoint.layer
.. autoattribute:: BasePoint.font

Identification
==============

.. autoattribute:: BasePoint.name
.. autoattribute:: BasePoint.identifier
.. autoattribute:: BasePoint.index

Coordinate
==========

.. autoattribute:: BasePoint.x
.. autoattribute:: BasePoint.y

Type
====

.. autoattribute:: BasePoint.type
.. autoattribute:: BasePoint.smooth

Transformations
===============

.. automethod:: BasePoint.transformBy
.. automethod:: BasePoint.moveBy
.. automethod:: BasePoint.scaleBy
.. automethod:: BasePoint.rotateBy
.. automethod:: BasePoint.skewBy

Normalization
=============

.. automethod:: BasePoint.round

Environment
===========

.. automethod:: BasePoint.naked
.. automethod:: BasePoint.changed
