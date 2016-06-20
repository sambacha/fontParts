.. highlight:: python
.. module:: fontParts.base

#########
Guideline
#########

********
Overview
********

Copy
====
* :meth:`~BaseGuideline.copy` (add general description)

Parents
=======
* :attr:`~BaseGuideline.glyph` (add general description)
* :attr:`~BaseGuideline.layer` (add general description)
* :attr:`~BaseGuideline.font` (add general description)

Identification
==============
* :attr:`~BaseGuideline.name` (add general description)
* :attr:`~BaseGuideline.color` (add general description)
* :attr:`~BaseGuideline.identifier` (add general description)
* :attr:`~BaseGuideline.index` (add general description)

Attributes
==========
* :attr:`~BaseGuideline.x` (add general description)
* :attr:`~BaseGuideline.y` (add general description)
* :attr:`~BaseGuideline.angle` (add general description)

Transformations
===============
* :meth:`~BaseGuideline.transformBy` (add general description)
* :meth:`~BaseGuideline.moveBy` (add general description)
* :meth:`~BaseGuideline.scaleBy` (add general description)
* :meth:`~BaseGuideline.rotateBy` (add general description)
* :meth:`~BaseGuideline.skewBy` (add general description)

Normalization
=============
* :meth:`~BaseGuideline.round` (add general description)

Environment
===========
* :meth:`~BaseGuideline.naked` (add general description)
* :meth:`~BaseGuideline.update` (add general description)


*********
Reference
*********

.. autoclass:: BaseGuideline

	.. autoattribute:: BaseGuideline.angle
	.. autoattribute:: BaseGuideline.color
	.. autoattribute:: BaseGuideline.font
	.. autoattribute:: BaseGuideline.glyph
	.. autoattribute:: BaseGuideline.identifier
	.. autoattribute:: BaseGuideline.index
	.. autoattribute:: BaseGuideline.layer
	.. autoattribute:: BaseGuideline.name
	.. autoattribute:: BaseGuideline.x
	.. autoattribute:: BaseGuideline.y
	.. automethod:: BaseGuideline.copy
	.. automethod:: BaseGuideline.moveBy
	.. automethod:: BaseGuideline.naked
	.. automethod:: BaseGuideline.rotateBy
	.. automethod:: BaseGuideline.round	
	.. automethod:: BaseGuideline.scaleBy
	.. automethod:: BaseGuideline.skewBy
	.. automethod:: BaseGuideline.transformBy
	.. automethod:: BaseGuideline.update