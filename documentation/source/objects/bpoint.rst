.. highlight:: python
.. module:: fontParts.base

######
bPoint
######

.. autoclass:: BaseBPoint

Parents
=======

.. autoattribute:: BaseBPoint.contour
.. autoattribute:: BaseBPoint.glyph
.. autoattribute:: BaseBPoint.layer
.. autoattribute:: BaseBPoint.font

Identification
==============

.. autoattribute:: BaseBPoint.index

Attributes
==========

.. autoattribute:: BaseBPoint.type

Points
======

.. autoattribute:: BaseBPoint.anchor
.. autoattribute:: BaseBPoint.bcpIn
.. autoattribute:: BaseBPoint.bcpOut

Transformations
===============

.. automethod:: BaseBPoint.transformBy
.. automethod:: BaseBPoint.moveBy
.. automethod:: BaseBPoint.scaleBy
.. automethod:: BaseBPoint.rotateBy
.. automethod:: BaseBPoint.skewBy

Normalization
=============

.. automethod:: BaseBPoint.round

Environment
===========

.. automethod:: BaseBPoint.naked
.. automethod:: BaseBPoint.changed
