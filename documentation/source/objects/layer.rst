.. highlight:: python
.. module:: fontParts.objects.base

=====
Layer
=====

Copy
""""
.. automethod:: BaseLayer.copy

Parents
"""""""
.. autoattribute:: BaseLayer.font

Copy
""""
.. automethod:: BaseLayer.copy

Attributes
""""""""""
.. autoattribute:: BaseLayer.name
.. autoattribute:: BaseLayer.color

Sub-Objects
"""""""""""
.. autoattribute:: BaseLayer.lib

Glyphs
""""""
.. automethod:: BaseLayer.__len__
.. automethod:: BaseLayer.keys
.. automethod:: BaseLayer.__iter__
.. automethod:: BaseLayer.__contains__
.. automethod:: BaseLayer.__getitem__
.. automethod:: BaseLayer.newGlyph
.. automethod:: BaseLayer.insertGlyph
.. automethod:: BaseLayer.removeGlyph

Interpolation
"""""""""""""
.. automethod:: BaseLayer.isCompatible
.. automethod:: BaseLayer.interpolate

Normalization
"""""""""""""
.. automethod:: BaseLayer.round
.. automethod:: BaseLayer.autoUnicodes

Environment
"""""""""""
.. automethod:: BaseLayer.naked
.. automethod:: BaseLayer.update
