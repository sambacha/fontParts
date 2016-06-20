.. highlight:: python
.. module:: fontParts.base

#####
Point
#####

********
Overview
********

Copy
====
* :meth:`~BasePoint.copy` (add general description)

Parents
=======
* :attr:`~BasePoint.contour` (add general description)
* :attr:`~BasePoint.glyph` (add general description)
* :attr:`~BasePoint.layer` (add general description)
* :attr:`~BasePoint.font` (add general description)

Identification
==============
* :attr:`~BasePoint.name` (add general description)
* :attr:`~BasePoint.identifier` (add general description)
* :attr:`~BasePoint.index` (add general description)

Attributes
==========
* :attr:`~BasePoint.type` (add general description)
* :attr:`~BasePoint.smooth` (add general description)
* :attr:`~BasePoint.x` (add general description)
* :attr:`~BasePoint.y` (add general description)

Transformations
===============
* :meth:`~BasePoint.transformBy` (add general description)
* :meth:`~BasePoint.moveBy` (add general description)
* :meth:`~BasePoint.scaleBy` (add general description)
* :meth:`~BasePoint.rotateBy` (add general description)
* :meth:`~BasePoint.skewBy` (add general description)

Normalization
=============
* :meth:`~BasePoint.round` (add general description)

Environment
===========
* :meth:`~BasePoint.naked` (add general description)
* :meth:`~BasePoint.update` (add general description)


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
	.. automethod:: BasePoint.update