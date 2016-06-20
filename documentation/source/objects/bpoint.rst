.. highlight:: python
.. module:: fontParts.base

######
bPoint
######

********
Overview
********

Parents
=======
* :attr:`~BaseBPoint.contour` (add general description)
* :attr:`~BaseBPoint.glyph` (add general description)
* :attr:`~BaseBPoint.layer` (add general description)
* :attr:`~BaseBPoint.font` (add general description)

Identification
==============
* :attr:`~BaseBPoint.index` (add general description)

Attributes
==========
* :attr:`~BaseBPoint.type` (add general description)

Points
======
* :attr:`~BaseBPoint.anchor` (add general description)
* :attr:`~BaseBPoint.bcpIn` (add general description)
* :attr:`~BaseBPoint.bcpOut` (add general description)

Transformations
===============
* :meth:`~BaseBPoint.transformBy` (add general description)
* :meth:`~BaseBPoint.moveBy` (add general description)
* :meth:`~BaseBPoint.scaleBy` (add general description)
* :meth:`~BaseBPoint.rotateBy` (add general description)
* :meth:`~BaseBPoint.skewBy` (add general description)

Normalization
=============
* :meth:`~BaseBPoint.round` (add general description)

Environment
===========
* :meth:`~BaseBPoint.naked` (add general description)
* :meth:`~BaseBPoint.update` (add general description)

*********
Reference
*********

.. autoclass:: BaseBPoint

	.. autoattribute:: BaseBPoint.anchor
	.. autoattribute:: BaseBPoint.bcpIn
	.. autoattribute:: BaseBPoint.bcpOut
	.. autoattribute:: BaseBPoint.contour
	.. autoattribute:: BaseBPoint.font
	.. autoattribute:: BaseBPoint.glyph
	.. autoattribute:: BaseBPoint.index
	.. autoattribute:: BaseBPoint.layer
	.. autoattribute:: BaseBPoint.type
	.. automethod:: BaseBPoint.moveBy
	.. automethod:: BaseBPoint.naked
	.. automethod:: BaseBPoint.rotateBy
	.. automethod:: BaseBPoint.round	
	.. automethod:: BaseBPoint.scaleBy
	.. automethod:: BaseBPoint.skewBy
	.. automethod:: BaseBPoint.transformBy
	.. automethod:: BaseBPoint.update