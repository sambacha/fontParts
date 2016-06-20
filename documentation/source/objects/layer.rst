.. highlight:: python
.. module:: fontParts.base

#####
Layer
#####

********
Overview
********


Copy
====
* :meth:`~BaseLayer.copy` (add general description)

Parents
=======
* :attr:`~BaseLayer.font` (add general description)

Attributes
==========
* :attr:`~BaseLayer.name` (add general description)
* :attr:`~BaseLayer.color` (add general description)

Sub-Objects
===========
* :attr:`~BaseLayer.lib` (add general description)

Glyphs
======
* :meth:`~BaseLayer.__len__` (add general description)
* :meth:`~BaseLayer.keys` (add general description)
* :meth:`~BaseLayer.__iter__` (add general description)
* :meth:`~BaseLayer.__contains__` (add general description)
* :meth:`~BaseLayer.__getitem__` (add general description)
* :meth:`~BaseLayer.newGlyph` (add general description)
* :meth:`~BaseLayer.insertGlyph` (add general description)
* :meth:`~BaseLayer.removeGlyph` (add general description)

Interpolation
=============
* :meth:`~BaseLayer.isCompatible` (add general description)
* :meth:`~BaseLayer.interpolate` (add general description)

Normalization
=============
* :meth:`~BaseLayer.round` (add general description)
* :meth:`~BaseLayer.autoUnicodes` (add general description)

Environment
===========
* :meth:`~BaseLayer.naked` (add general description)
* :meth:`~BaseLayer.update` (add general description)

*********
Reference
*********

.. autoclass:: BaseLayer

	.. autoattribute:: BaseLayer.color
	.. autoattribute:: BaseLayer.font
	.. autoattribute:: BaseLayer.lib
	.. autoattribute:: BaseLayer.name
	.. automethod:: BaseLayer.__contains__
	.. automethod:: BaseLayer.__getitem__
	.. automethod:: BaseLayer.__iter__
	.. automethod:: BaseLayer.__len__
	.. automethod:: BaseLayer.autoUnicodes
	.. automethod:: BaseLayer.copy
	.. automethod:: BaseLayer.insertGlyph
	.. automethod:: BaseLayer.interpolate
	.. automethod:: BaseLayer.isCompatible
	.. automethod:: BaseLayer.keys
	.. automethod:: BaseLayer.naked
	.. automethod:: BaseLayer.newGlyph
	.. automethod:: BaseLayer.removeGlyph
	.. automethod:: BaseLayer.round
	.. automethod:: BaseLayer.update