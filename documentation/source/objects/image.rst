.. highlight:: python
.. module:: fontParts.base

#####
Image
#####

********
Overview
********

Copy
====
* :meth:`~BaseImage.copy` (add general description)

Parents
=======
* :attr:`~BaseImage.glyph` (add general description)
* :attr:`~BaseImage.layer` (add general description)
* :attr:`~BaseImage.font` (add general description)

Attributes
==========
* :attr:`~BaseImage.data` (add general description)
* :attr:`~BaseImage.color` (add general description)
* :attr:`~BaseImage.transformation` (add general description)
* :attr:`~BaseImage.offset` (add general description)
* :attr:`~BaseImage.scale` (add general description)

Transformations
===============
* :meth:`~BaseImage.transformBy` (add general description)
* :meth:`~BaseImage.moveBy` (add general description)
* :meth:`~BaseImage.scaleBy` (add general description)
* :meth:`~BaseImage.rotateBy` (add general description)
* :meth:`~BaseImage.skewBy` (add general description)

Normalization
=============
* :meth:`~BaseImage.round` (add general description)

Environment
===========
* :meth:`~BaseImage.naked` (add general description)
* :meth:`~BaseImage.update` (add general description)


*********
Reference
*********

.. autoclass:: BaseImage

	.. autoattribute:: BaseImage.color
	.. autoattribute:: BaseImage.data
	.. autoattribute:: BaseImage.font
	.. autoattribute:: BaseImage.glyph
	.. autoattribute:: BaseImage.layer
	.. autoattribute:: BaseImage.offset
	.. autoattribute:: BaseImage.scale
	.. autoattribute:: BaseImage.transformation
	.. automethod:: BaseImage.copy
	.. automethod:: BaseImage.moveBy
	.. automethod:: BaseImage.naked
	.. automethod:: BaseImage.rotateBy
	.. automethod:: BaseImage.round
	.. automethod:: BaseImage.scaleBy
	.. automethod:: BaseImage.skewBy
	.. automethod:: BaseImage.transformBy
	.. automethod:: BaseImage.update