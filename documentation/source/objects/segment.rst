.. highlight:: python
.. module:: fontParts.base

#######
Segment
#######

.. autoclass:: BaseSegment

Parents
=======

.. autoattribute:: BaseSegment.contour
.. autoattribute:: BaseSegment.glyph
.. autoattribute:: BaseSegment.layer
.. autoattribute:: BaseSegment.font

Identification
==============

.. autoattribute:: BaseSegment.index

Attributes
==========

.. autoattribute:: BaseSegment.type
.. autoattribute:: BaseSegment.smooth

Points
======

.. autoattribute:: BaseSegment.points
.. autoattribute:: BaseSegment.onCurve
.. autoattribute:: BaseSegment.offCurve

Transformations
===============

.. automethod:: BaseSegment.transformBy
.. automethod:: BaseSegment.moveBy
.. automethod:: BaseSegment.scaleBy
.. automethod:: BaseSegment.rotateBy
.. automethod:: BaseSegment.skewBy

Normalization
=============

.. automethod:: BaseSegment.round

Environment
===========

.. automethod:: BaseSegment.naked
.. automethod:: BaseSegment.changed

