.. highlight:: python
.. module:: fontParts.base

====
Font
====

Constructor
"""""""""""
.. automethod:: BaseFont.__init__

Copy
""""
.. automethod:: BaseFont.copy

File Operations
"""""""""""""""
.. autoattribute:: BaseFont.path
.. automethod:: BaseFont.save
.. automethod:: BaseFont.close
.. automethod:: BaseFont.generate

Sub-Objects
"""""""""""
.. autoattribute:: BaseFont.info
.. autoattribute:: BaseFont.groups
.. autoattribute:: BaseFont.kerning
.. autoattribute:: BaseFont.features
.. autoattribute:: BaseFont.lib

Layers
""""""
.. autoattribute:: BaseFont.layers
.. autoattribute:: BaseFont.layerOrder
.. autoattribute:: BaseFont.defaultLayer
.. automethod:: BaseFont.getLayer
.. automethod:: BaseFont.newLayer
.. automethod:: BaseFont.removeLayer

Glyphs
""""""

Interacting with glyphs at the font level is a shortcut for interacting with glyphs in the default layer.

	>>> glyph = font.newGlyph("A")

Does the same thing as:

	>>> glyph = font.getLayer(font.defaultLayer).newGlyph("A")

.. automethod:: BaseFont.__len__
.. automethod:: BaseFont.keys
.. autoattribute:: BaseFont.glyphOrder
.. automethod:: BaseFont.__iter__
.. automethod:: BaseFont.__contains__
.. automethod:: BaseFont.__getitem__
.. automethod:: BaseFont.newGlyph
.. automethod:: BaseFont.insertGlyph
.. automethod:: BaseFont.removeGlyph

Guidelines
""""""""""
.. autoattribute:: BaseFont.guidelines
.. automethod:: BaseFont.appendGuideline
.. automethod:: BaseFont.removeGuideline
.. automethod:: BaseFont.clearGuidelines

Interpolation
"""""""""""""
.. automethod:: BaseFont.isCompatible
.. automethod:: BaseFont.interpolate

Normalization
"""""""""""""
.. automethod:: BaseFont.round
.. automethod:: BaseFont.autoUnicodes

Environment
"""""""""""
.. automethod:: BaseFont.naked
.. automethod:: BaseFont.update
