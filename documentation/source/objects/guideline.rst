.. highlight:: python
.. module:: fontParts.objects.base

=========
Guideline
=========

Parents
"""""""
.. autoattribute:: BaseGuideline.glyph
.. autoattribute:: BaseGuideline.layer
.. autoattribute:: BaseGuideline.font

Identification
""""""""""""""
.. autoattribute:: BaseGuideline.name
.. autoattribute:: BaseGuideline.color
.. autoattribute:: BaseGuideline.identifier
.. autoattribute:: BaseGuideline.index

Attributes
""""""""""
.. autoattribute:: BaseGuideline.x
.. autoattribute:: BaseGuideline.y
.. autoattribute:: BaseGuideline.angle

Transformations
"""""""""""""""
.. automethod:: BaseGuideline.transformBy
.. automethod:: BaseGuideline.moveBy
.. automethod:: BaseGuideline.scaleBy
.. automethod:: BaseGuideline.rotateBy
.. automethod:: BaseGuideline.skewBy

Normalization
"""""""""""""
.. automethod:: BaseGuideline.round	

Environment
"""""""""""
.. automethod:: BaseGuideline.naked
.. automethod:: BaseGuideline.update