.. highlight:: python
.. module:: fontParts.objects.base

=======
Contour
=======

Copy
""""
.. automethod:: BaseContour.copy

Parents
"""""""
.. autoattribute:: BaseContour.glyph
.. autoattribute:: BaseContour.layer
.. autoattribute:: BaseContour.font

Identification
""""""""""""""
.. autoattribute:: BaseContour.identifier
.. autoattribute:: BaseContour.index

Winding Direction
"""""""""""""""""
.. autoattribute:: BaseContour.clockwise
.. automethod:: BaseContour.reverse

Queries
"""""""
.. autoattribute:: BaseContour.bounds
.. automethod:: BaseContour.pointInside

Pens and Drawing
""""""""""""""""
.. automethod:: BaseContour.draw
.. automethod:: BaseContour.drawPoints

Segments
""""""""
.. autoattribute:: BaseContour.segments
.. automethod:: BaseContour.__len__
.. automethod:: BaseContour.__iter__
.. automethod:: BaseContour.__getitem__
.. automethod:: BaseContour.appendSegment
.. automethod:: BaseContour.insertSegment
.. automethod:: BaseContour.removeSegment
.. automethod:: BaseContour.setStartSegment
.. automethod:: BaseContour.autoStartSegment

bPoints
"""""""
.. autoattribute:: BaseContour.bPoints
.. automethod:: BaseContour.appendBPoint
.. automethod:: BaseContour.insertBPoint

Points
""""""
.. autoattribute:: BaseContour.points
.. automethod:: BaseContour.appendPoint
.. automethod:: BaseContour.insertPoint
.. automethod:: BaseContour.removePoint

Transformations
"""""""""""""""
.. automethod:: BaseContour.transformBy
.. automethod:: BaseContour.moveBy
.. automethod:: BaseContour.scaleBy
.. automethod:: BaseContour.rotateBy
.. automethod:: BaseContour.skewBy

Normalization
"""""""""""""
.. automethod:: BaseContour.round	

Environment
"""""""""""
.. automethod:: BaseContour.naked
.. automethod:: BaseContour.update
