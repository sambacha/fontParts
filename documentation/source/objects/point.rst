.. highlight:: python
.. module:: fontParts.base

=====
Point
=====

Copy
""""
.. automethod:: BasePoint.copy

Parents
"""""""
.. autoattribute:: BasePoint.contour
.. autoattribute:: BasePoint.glyph
.. autoattribute:: BasePoint.layer
.. autoattribute:: BasePoint.font

Identification
""""""""""""""
.. autoattribute:: BasePoint.name
.. autoattribute:: BasePoint.identifier
.. autoattribute:: BasePoint.index

Attributes
""""""""""
.. autoattribute:: BasePoint.type
.. autoattribute:: BasePoint.smooth
.. autoattribute:: BasePoint.x
.. autoattribute:: BasePoint.y

Transformations
"""""""""""""""
.. automethod:: BasePoint.transformBy
.. automethod:: BasePoint.moveBy
.. automethod:: BasePoint.scaleBy
.. automethod:: BasePoint.rotateBy
.. automethod:: BasePoint.skewBy

Normalization
"""""""""""""
.. automethod:: BasePoint.round	

Environment
"""""""""""
.. automethod:: BasePoint.naked
.. automethod:: BasePoint.update
