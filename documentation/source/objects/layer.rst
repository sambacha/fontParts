.. highlight:: python
.. module:: fontParts.base

#####
Layer
#####

********
Overview
********

.. note::

	This section needs to contain the following:

	* description of what this is
	* sub-object with basic usage
	* glyph interaction with basic usage

Copy
====
* :meth:`~BaseLayer.copy` Copy the layer.

Parents
=======
* :attr:`~BaseLayer.font` The layer's parent :class`BaseFont`.

Attributes
==========
* :attr:`~BaseLayer.name` The name of the layer.
* :attr:`~BaseLayer.color` The color of the layer.

Sub-Objects
===========
* :attr:`~BaseLayer.lib` The layer's :class:`BaseLib`.

Glyphs
======
* :meth:`~BaseLayer.__len__` The number of glyphs in the layer.
* :meth:`~BaseLayer.keys` The names of all glyphs in the layer.
* :meth:`~BaseLayer.__iter__` Iterate over all :class:`BaseGlyph` objects in the layer.
* :meth:`~BaseLayer.__contains__` Determine if a particular glyph is in the layer.
* :meth:`~BaseLayer.__getitem__` Get a particular glyph from the layer.
* :meth:`~BaseLayer.newGlyph` Create a glyph in the layer.
* :meth:`~BaseLayer.insertGlyph` Insert a glyph into the layer.
* :meth:`~BaseLayer.removeGlyph` Remove a glyph from the layer.

Interpolation
=============
* :meth:`~BaseLayer.isCompatible` Determine if one layer is compatible for interpolation with another.
* :meth:`~BaseLayer.interpolate` Interpolate this layer between two other layers.

Normalization
=============
* :meth:`~BaseLayer.round` Round coordinates in the layer.
* :meth:`~BaseLayer.autoUnicodes` Guess Unicode values for all glyphs in the layer.

Environment
===========
* :meth:`~BaseLayer.naked` Get the environment’s native layer object.
* :meth:`~BaseLayer.update` Inform the environment to update the layer.

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