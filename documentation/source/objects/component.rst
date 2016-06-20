.. highlight:: python
.. module:: fontParts.base

#########
Component
#########

********
Overview
********

Copy
====
* :meth:`~BaseComponent.copy` (add general description)

Parents
=======
* :attr:`~BaseComponent.glyph` (add general description)
* :attr:`~BaseComponent.layer` (add general description)
* :attr:`~BaseComponent.font` (add general description)

Identification
==============
* :attr:`~BaseComponent.identifier` (add general description)
* :attr:`~BaseComponent.index` (add general description)

Attributes
==========
* :attr:`~BaseComponent.baseGlyph` (add general description)
* :attr:`~BaseComponent.transformation` (add general description)
* :attr:`~BaseComponent.offset` (add general description)
* :attr:`~BaseComponent.scale` (add general description)

Queries
=======
* :attr:`~BaseComponent.bounds` (add general description)
* :meth:`~BaseComponent.pointInside` (add general description)

Pens and Drawing
================
* :meth:`~BaseComponent.draw` (add general description)
* :meth:`~BaseComponent.drawPoints` (add general description)

Transformations
===============
* :meth:`~BaseComponent.transformBy` (add general description)
* :meth:`~BaseComponent.moveBy` (add general description)
* :meth:`~BaseComponent.scaleBy` (add general description)
* :meth:`~BaseComponent.rotateBy` (add general description)
* :meth:`~BaseComponent.skewBy` (add general description)

Normalization
=============
* :meth:`~BaseComponent.decompose` (add general description)
* :meth:`~BaseComponent.round` (add general description)

Environment
===========
* :meth:`~BaseComponent.naked` (add general description)
* :meth:`~BaseComponent.update` (add general description)

*********
Reference
*********

.. autoclass:: BaseComponent

	.. autoattribute:: BaseComponent.baseGlyph
	.. autoattribute:: BaseComponent.bounds
	.. autoattribute:: BaseComponent.font
	.. autoattribute:: BaseComponent.glyph
	.. autoattribute:: BaseComponent.identifier
	.. autoattribute:: BaseComponent.index
	.. autoattribute:: BaseComponent.layer
	.. autoattribute:: BaseComponent.offset
	.. autoattribute:: BaseComponent.scale
	.. autoattribute:: BaseComponent.transformation
	.. automethod:: BaseComponent.copy
	.. automethod:: BaseComponent.decompose
	.. automethod:: BaseComponent.draw
	.. automethod:: BaseComponent.drawPoints
	.. automethod:: BaseComponent.moveBy
	.. automethod:: BaseComponent.naked
	.. automethod:: BaseComponent.pointInside
	.. automethod:: BaseComponent.rotateBy
	.. automethod:: BaseComponent.round
	.. automethod:: BaseComponent.scaleBy
	.. automethod:: BaseComponent.skewBy
	.. automethod:: BaseComponent.transformBy
	.. automethod:: BaseComponent.update