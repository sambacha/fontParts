.. highlight:: python
.. module:: fontParts.base

#######
Contour
#######

********
Overview
********

Copy
====
* :meth:`~BaseContour.copy` (add general description)

Parents
=======
* :attr:`~BaseContour.glyph` (add general description)
* :attr:`~BaseContour.layer` (add general description)
* :attr:`~BaseContour.font` (add general description)

Identification
==============
* :attr:`~BaseContour.identifier` (add general description)
* :attr:`~BaseContour.index` (add general description)

Winding Direction
=================
* :attr:`~BaseContour.clockwise` (add general description)
* :meth:`~BaseContour.reverse` (add general description)

Queries
=======
* :attr:`~BaseContour.bounds` (add general description)
* :meth:`~BaseContour.pointInside` (add general description)

Pens and Drawing
================
* :meth:`~BaseContour.draw` (add general description)
* :meth:`~BaseContour.drawPoints` (add general description)

Segments
========
* :attr:`~BaseContour.segments` (add general description)
* :meth:`~BaseContour.__len__` (add general description)
* :meth:`~BaseContour.__iter__` (add general description)
* :meth:`~BaseContour.__getitem__` (add general description)
* :meth:`~BaseContour.appendSegment` (add general description)
* :meth:`~BaseContour.insertSegment` (add general description)
* :meth:`~BaseContour.removeSegment` (add general description)
* :meth:`~BaseContour.setStartSegment` (add general description)
* :meth:`~BaseContour.autoStartSegment` (add general description)

bPoints
=======
* :attr:`~BaseContour.bPoints` (add general description)
* :meth:`~BaseContour.appendBPoint` (add general description)
* :meth:`~BaseContour.insertBPoint` (add general description)

Points
======
* :attr:`~BaseContour.points` (add general description)
* :meth:`~BaseContour.appendPoint` (add general description)
* :meth:`~BaseContour.insertPoint` (add general description)
* :meth:`~BaseContour.removePoint` (add general description)

Transformations
===============
* :meth:`~BaseContour.transformBy` (add general description)
* :meth:`~BaseContour.moveBy` (add general description)
* :meth:`~BaseContour.scaleBy` (add general description)
* :meth:`~BaseContour.rotateBy` (add general description)
* :meth:`~BaseContour.skewBy` (add general description)

Normalization
=============
* :meth:`~BaseContour.round` (add general description)

Environment
===========
* :meth:`~BaseContour.naked` (add general description)
* :meth:`~BaseContour.changed` (add general description)


*********
Reference
*********

.. autoclass:: BaseContour

	.. autoattribute:: BaseContour.bPoints
	.. autoattribute:: BaseContour.bounds
	.. autoattribute:: BaseContour.clockwise
	.. autoattribute:: BaseContour.font
	.. autoattribute:: BaseContour.glyph
	.. autoattribute:: BaseContour.identifier
	.. autoattribute:: BaseContour.index
	.. autoattribute:: BaseContour.layer
	.. autoattribute:: BaseContour.points
	.. autoattribute:: BaseContour.segments
	.. automethod:: BaseContour.__getitem__
	.. automethod:: BaseContour.__iter__
	.. automethod:: BaseContour.__len__
	.. automethod:: BaseContour.appendBPoint
	.. automethod:: BaseContour.appendPoint
	.. automethod:: BaseContour.appendSegment
	.. automethod:: BaseContour.autoStartSegment
	.. automethod:: BaseContour.copy
	.. automethod:: BaseContour.draw
	.. automethod:: BaseContour.drawPoints
	.. automethod:: BaseContour.insertBPoint
	.. automethod:: BaseContour.insertPoint
	.. automethod:: BaseContour.insertSegment
	.. automethod:: BaseContour.moveBy
	.. automethod:: BaseContour.naked
	.. automethod:: BaseContour.pointInside
	.. automethod:: BaseContour.removePoint
	.. automethod:: BaseContour.removeSegment
	.. automethod:: BaseContour.reverse
	.. automethod:: BaseContour.rotateBy
	.. automethod:: BaseContour.round	
	.. automethod:: BaseContour.scaleBy
	.. automethod:: BaseContour.setStartSegment
	.. automethod:: BaseContour.skewBy
	.. automethod:: BaseContour.transformBy
	.. automethod:: BaseContour.changed