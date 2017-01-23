.. highlight:: python
.. module:: fontParts.base

#########
Component
#########

.. autoclass:: BaseComponent

Parents
=======

.. autoattribute:: BaseComponent.glyph
.. autoattribute:: BaseComponent.layer
.. autoattribute:: BaseComponent.font

Copy
====

.. automethod:: BaseComponent.copy

Identification
==============

.. autoattribute:: BaseComponent.identifier
.. autoattribute:: BaseComponent.index

Attributes
==========

.. autoattribute:: BaseComponent.baseGlyph
.. autoattribute:: BaseComponent.transformation
.. autoattribute:: BaseComponent.offset
.. autoattribute:: BaseComponent.scale

Queries
=======

.. autoattribute:: BaseComponent.bounds
.. automethod:: BaseComponent.pointInside

Pens and Drawing
================

.. automethod:: BaseComponent.draw
.. automethod:: BaseComponent.drawPoints

Transformations
===============

.. automethod:: BaseComponent.transformBy
.. automethod:: BaseComponent.moveBy
.. automethod:: BaseComponent.scaleBy
.. automethod:: BaseComponent.rotateBy
.. automethod:: BaseComponent.skewBy

Normalization
=============

.. automethod:: BaseComponent.decompose
.. automethod:: BaseComponent.round

Environment
===========

.. automethod:: BaseComponent.naked
.. automethod:: BaseComponent.changed
