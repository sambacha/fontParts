.. highlight:: python
.. module:: fontParts.base

####
Font
####

********
Overview
********

.. note::

	This section needs to contain the following:

	* description of what this is
	* sub-object with basic usage
	* bridge to default layer for glyphs for backwards compatibility
	* glyph interaction with basic usage

Copy
====

* :meth:`~BaseFont.copy` Copy the font.

File Operations
===============

* :attr:`~BaseFont.path` The path to the font's file on disk.
* :meth:`~BaseFont.save` Save the font to disk.
* :meth:`~BaseFont.close` Close the font.
* :meth:`~BaseFont.generate` Generate the font to another file format.

Sub-Objects
===========

* :attr:`~BaseFont.info` The font's :class:`BaseInfo`.
* :attr:`~BaseFont.groups` The font's :class:`BaseGroups`.
* :attr:`~BaseFont.kerning` The font's :class:`BaseKerning`.
* :attr:`~BaseFont.features` The font's :class:`BaseFeatures`.
* :attr:`~BaseFont.lib` The font's :class:`BaseLib`.

Layers
======

* :attr:`~BaseFont.layers` The font's :class:`BaseLayer` objects.
* :attr:`~BaseFont.layerOrder` The font's layer order.
* :attr:`~BaseFont.defaultLayer` The name of the font's default layer.
* :meth:`~BaseFont.getLayer` Get a particular layer from the font.
* :meth:`~BaseFont.newLayer` Create a layer in the font.
* :meth:`~BaseFont.removeLayer` Remove a layer from the font.

Glyphs
======

Interacting with glyphs at the font level is a shortcut for interacting with glyphs in the default layer. ::

	>>> glyph = font.newGlyph("A")

Does the same thing as::

	>>> glyph = font.getLayer(font.defaultLayer).newGlyph("A")

* :meth:`~BaseFont.__len__` The number of glyphs in the default layer.
* :meth:`~BaseFont.keys` The names of all glyphs in the default layer.
* :attr:`~BaseFont.glyphOrder` The order of all glyphs in the font.
* :meth:`~BaseFont.__iter__` Iterate over all :class:`BaseGlyph` objects in the default layer.
* :meth:`~BaseFont.__contains__` Determine if a particular glyph is in the default layer.
* :meth:`~BaseFont.__getitem__` Get a particular glyph from the default layer.
* :meth:`~BaseFont.newGlyph` Create a glyph in the default layer.
* :meth:`~BaseFont.insertGlyph` Insert a glyph into the default layer.
* :meth:`~BaseFont.removeGlyph` Remove a glyph from the default layer.

Guidelines
==========

* :attr:`~BaseFont.guidelines` A list of all font level :class:`BaseGuideline` objects.
* :meth:`~BaseFont.appendGuideline` Append a guideline to the font.
* :meth:`~BaseFont.removeGuideline` Remove a guideline from the font.
* :meth:`~BaseFont.clearGuidelines` Clear all guidelines in the font.

Interpolation
=============

* :meth:`~BaseFont.isCompatible` Determine if one font is compatible for interpolation with another.
* :meth:`~BaseFont.interpolate` Interpolate this font between two other fonts.

Normalization
=============

* :meth:`~BaseFont.round` Round coordinates in the font.
* :meth:`~BaseFont.autoUnicodes` Guess Unicode values for all glyphs in the default layer.

Environment
===========

* :meth:`~BaseFont.naked` Get the environment's native font object.
* :meth:`~BaseFont.changed` Inform the environment to update the font.


*********
Reference
*********

.. autoclass:: BaseFont

	.. autoattribute:: BaseFont.defaultLayer
	.. autoattribute:: BaseFont.features
	.. autoattribute:: BaseFont.glyphOrder
	.. autoattribute:: BaseFont.groups
	.. autoattribute:: BaseFont.guidelines
	.. autoattribute:: BaseFont.info
	.. autoattribute:: BaseFont.kerning
	.. autoattribute:: BaseFont.layerOrder
	.. autoattribute:: BaseFont.layers
	.. autoattribute:: BaseFont.lib
	.. autoattribute:: BaseFont.path
	.. automethod:: BaseFont.__contains__
	.. automethod:: BaseFont.__getitem__
	.. automethod:: BaseFont.__iter__
	.. automethod:: BaseFont.__len__
	.. automethod:: BaseFont.appendGuideline
	.. automethod:: BaseFont.autoUnicodes
	.. automethod:: BaseFont.clearGuidelines
	.. automethod:: BaseFont.close
	.. automethod:: BaseFont.copy
	.. automethod:: BaseFont.generate
	.. automethod:: BaseFont.getLayer
	.. automethod:: BaseFont.insertGlyph
	.. automethod:: BaseFont.interpolate
	.. automethod:: BaseFont.isCompatible
	.. automethod:: BaseFont.keys
	.. automethod:: BaseFont.naked
	.. automethod:: BaseFont.newGlyph
	.. automethod:: BaseFont.newLayer
	.. automethod:: BaseFont.removeGlyph
	.. automethod:: BaseFont.removeGuideline
	.. automethod:: BaseFont.removeLayer
	.. automethod:: BaseFont.round
	.. automethod:: BaseFont.save
	.. automethod:: BaseFont.changed
