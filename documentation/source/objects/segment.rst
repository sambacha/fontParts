.. highlight:: python
.. module:: fontParts.base

#######
Segment
#######

********
Overview
********

Parents
=======
* :attr:`~BaseSegment.contour` (add general description)
* :attr:`~BaseSegment.glyph` (add general description)
* :attr:`~BaseSegment.layer` (add general description)
* :attr:`~BaseSegment.font` (add general description)

Identification
==============
* :attr:`~BaseSegment.index` (add general description)

Attributes
==========
* :attr:`~BaseSegment.type` (add general description)
* :attr:`~BaseSegment.smooth` (add general description)

Points
======
* :attr:`~BaseSegment.points` (add general description)
* :attr:`~BaseSegment.onCurve` (add general description)
* :attr:`~BaseSegment.offCurve` (add general description)

Transformations
===============
* :meth:`~BaseSegment.transformBy` (add general description)
* :meth:`~BaseSegment.moveBy` (add general description)
* :meth:`~BaseSegment.scaleBy` (add general description)
* :meth:`~BaseSegment.rotateBy` (add general description)
* :meth:`~BaseSegment.skewBy` (add general description)

Normalization
=============
* :meth:`~BaseSegment.round` (add general description)

Environment
===========
* :meth:`~BaseSegment.naked` (add general description)
* :meth:`~BaseSegment.update` (add general description)


*********
Reference
*********

.. autoclass:: BaseSegment

	.. autoattribute:: BaseSegment.contour
	.. autoattribute:: BaseSegment.font
	.. autoattribute:: BaseSegment.glyph
	.. autoattribute:: BaseSegment.index
	.. autoattribute:: BaseSegment.layer
	.. autoattribute:: BaseSegment.offCurve
	.. autoattribute:: BaseSegment.onCurve
	.. autoattribute:: BaseSegment.points
	.. autoattribute:: BaseSegment.smooth
	.. autoattribute:: BaseSegment.type
	.. automethod:: BaseSegment.moveBy
	.. automethod:: BaseSegment.naked
	.. automethod:: BaseSegment.rotateBy
	.. automethod:: BaseSegment.round	
	.. automethod:: BaseSegment.scaleBy
	.. automethod:: BaseSegment.skewBy
	.. automethod:: BaseSegment.transformBy
	.. automethod:: BaseSegment.update
