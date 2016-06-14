.. highlight:: python
.. module:: fontParts.base

======
Anchor
======

Copy
""""
.. automethod:: BaseAnchor.copy

Parents
"""""""
.. autoattribute:: BaseAnchor.glyph
.. autoattribute:: BaseAnchor.layer
.. autoattribute:: BaseAnchor.font

Identification
""""""""""""""
.. autoattribute:: BaseAnchor.name
.. autoattribute:: BaseAnchor.color
.. autoattribute:: BaseAnchor.identifier
.. autoattribute:: BaseAnchor.index

Attributes
""""""""""
.. autoattribute:: BaseAnchor.x
.. autoattribute:: BaseAnchor.y

Transformations
"""""""""""""""
.. automethod:: BaseAnchor.transformBy
.. automethod:: BaseAnchor.moveBy
.. automethod:: BaseAnchor.scaleBy
.. automethod:: BaseAnchor.rotateBy
.. automethod:: BaseAnchor.skewBy

Normalization
"""""""""""""
.. automethod:: BaseAnchor.round	

Environment
"""""""""""
.. automethod:: BaseAnchor.naked
.. automethod:: BaseAnchor.update