.. highlight:: python
.. module:: fontParts.base

#########
Component
#########

********
Overview
********

Copy
====

* :meth:`~BaseComponent.copy` Copy the component.

Parents
=======

* :attr:`~BaseComponent.glyph` The component's parent :class:`BaseGlyph`.
* :attr:`~BaseComponent.layer` The component's parent :class:`BaseLayer`.
* :attr:`~BaseComponent.font` The component's parent :class:`BaseFont`.

Identification
==============

* :attr:`~BaseComponent.identifier` The identifier of the component.
* :attr:`~BaseComponent.index` The index of the component within the parent glyph's ordered list of components.

Attributes
==========

* :attr:`~BaseComponent.baseGlyph` The name of the glyph the component points to. The glyph is assumed to be present in the same **font layer**. (XXX is this correct?)
* :attr:`~BaseComponent.transformation` The transformation matrix of the component.
* :attr:`~BaseComponent.offset` The offset vector. The distance the component has been moved.
* :attr:`~BaseComponent.scale` The scale of the component.

Queries
=======

* :attr:`~BaseComponent.bounds` The component's bounding box. The values are ``(xMin, yMin, xMax, yMax)``.
* :meth:`~BaseComponent.pointInside` Returns ``True`` if the point is inside the "black" area of the component or ``False`` if the point is inside the "white" area of the component.

Pens and Drawing
================

* :meth:`~BaseComponent.draw` Get this component to draw itself with the pen on offer.
* :meth:`~BaseComponent.drawPoints` Get this component to draw itself with the points pen on offer.

Transformations
===============

* :meth:`~BaseComponent.transformBy` Transform the component with a transformation matrix.
* :meth:`~BaseComponent.moveBy` Move the component.
* :meth:`~BaseComponent.scaleBy` Scale the component.
* :meth:`~BaseComponent.rotateBy` Rotate the component.
* :meth:`~BaseComponent.skewBy` Skew the component.

Normalization
=============

* :meth:`~BaseComponent.decompose` Replace the component object with its actual contours.
* :meth:`~BaseComponent.round` Round offset coordinates.

Environment
===========

* :meth:`~BaseComponent.naked` Get the environment's native component object.
* :meth:`~BaseComponent.changed` Inform the environment to update the component.

*********
Reference
*********

.. autoclass:: BaseComponent

	.. autoattribute:: BaseComponent.baseGlyph
	.. autoattribute:: BaseComponent.bounds
	.. autoattribute:: BaseComponent.font
	.. autoattribute:: BaseComponent.glyph
	.. autoattribute:: BaseComponent.identifier
	.. autoattribute:: BaseComponent.index
	.. autoattribute:: BaseComponent.layer
	.. autoattribute:: BaseComponent.offset
	.. autoattribute:: BaseComponent.scale
	.. autoattribute:: BaseComponent.transformation
	.. automethod:: BaseComponent.copy
	.. automethod:: BaseComponent.decompose
	.. automethod:: BaseComponent.draw
	.. automethod:: BaseComponent.drawPoints
	.. automethod:: BaseComponent.moveBy
	.. automethod:: BaseComponent.naked
	.. automethod:: BaseComponent.pointInside
	.. automethod:: BaseComponent.rotateBy
	.. automethod:: BaseComponent.round
	.. automethod:: BaseComponent.scaleBy
	.. automethod:: BaseComponent.skewBy
	.. automethod:: BaseComponent.transformBy
	.. automethod:: BaseComponent.changed