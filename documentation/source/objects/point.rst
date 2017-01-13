.. highlight:: python
.. module:: fontParts.base

#####
Point
#####

********
Overview
********

Points are single points in a contour. These can be on-curve or off-curve and they have various possible attributes.

::

	glyph = CurrentGlyph()
	for contour in glyph:
	    for point in contour.points:
	        print point

Copy
====
* :meth:`~BasePoint.copy` Copy the point.

Parents
=======
* :attr:`~BasePoint.contour` The point's parent :class:`BaseContour`.
* :attr:`~BasePoint.glyph` The point's parent :class:`BaseGlyph`.
* :attr:`~BasePoint.layer` The point's parent :class:`BaseLayer`.
* :attr:`~BasePoint.font` The point's parent :class:`BaseFont`.

Identification
==============
* :attr:`~BasePoint.name` The name of the point.
* :attr:`~BasePoint.identifier` The identifier of the point.
* :attr:`~BasePoint.index` The index of the point with the parent contour's ordered list of points.

Coordinate
==========
* :attr:`~BasePoint.x` The x position of the point.
* :attr:`~BasePoint.y` The y position of the point.

Type
====
* :attr:`~BasePoint.type` The type of the point.
* :attr:`~BasePoint.smooth` The curvature smoothing setting of the point.

Transformations
===============
* :meth:`~BasePoint.transformBy` Transform the point with a transformation matrix.
* :meth:`~BasePoint.moveBy` Move the point.
* :meth:`~BasePoint.scaleBy` Scale the point.
* :meth:`~BasePoint.rotateBy` Rotate the point.
* :meth:`~BasePoint.skewBy` Skew the point.

Normalization
=============
* :meth:`~BasePoint.round` Round the point.

Environment
===========
* :meth:`~BasePoint.naked` Get the environment's native point object.
* :meth:`~BasePoint.changed` Inform the environment to update the point.


*********
Reference
*********

.. autoclass:: BasePoint

	.. autoattribute:: BasePoint.contour
	.. autoattribute:: BasePoint.font
	.. autoattribute:: BasePoint.glyph
	.. autoattribute:: BasePoint.identifier
	.. autoattribute:: BasePoint.index
	.. autoattribute:: BasePoint.layer
	.. autoattribute:: BasePoint.name
	.. autoattribute:: BasePoint.smooth
	.. autoattribute:: BasePoint.type
	.. autoattribute:: BasePoint.x
	.. autoattribute:: BasePoint.y
	.. automethod:: BasePoint.copy
	.. automethod:: BasePoint.moveBy
	.. automethod:: BasePoint.naked
	.. automethod:: BasePoint.rotateBy
	.. automethod:: BasePoint.round	
	.. automethod:: BasePoint.scaleBy
	.. automethod:: BasePoint.skewBy
	.. automethod:: BasePoint.transformBy
	.. automethod:: BasePoint.changed