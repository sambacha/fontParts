.. highlight:: python
.. module:: fontParts.base

=====
Image
=====

Copy
""""
.. automethod:: BaseImage.copy

Parents
"""""""
.. autoattribute:: BaseImage.glyph
.. autoattribute:: BaseImage.layer
.. autoattribute:: BaseImage.font

Attributes
""""""""""
.. autoattribute:: BaseImage.data
.. autoattribute:: BaseImage.color
.. autoattribute:: BaseImage.transformation
.. autoattribute:: BaseImage.offset
.. autoattribute:: BaseImage.scale

Transformations
"""""""""""""""
.. automethod:: BaseImage.transformBy
.. automethod:: BaseImage.moveBy
.. automethod:: BaseImage.scaleBy
.. automethod:: BaseImage.rotateBy
.. automethod:: BaseImage.skewBy

Normalization
"""""""""""""
.. automethod:: BaseImage.round

Environment
"""""""""""
.. automethod:: BaseImage.naked
.. automethod:: BaseImage.update