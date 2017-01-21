.. highlight:: python
.. module:: fontParts.base

######
bPoint
######

********
Overview
********

Parents
=======
* :attr:`~BaseBPoint.contour` The point's parent :class:`BaseContour`.
* :attr:`~BaseBPoint.glyph` The point's parent :class:`BaseGlyph`.
* :attr:`~BaseBPoint.layer` The point's parent :class:`BaseLayer`.
* :attr:`~BaseBPoint.font` The point's parent :class:`BaseFont`.

Identification
==============
* :attr:`~BaseBPoint.index` The index of the bPoint with the parent contour's ordered list of bPoints.

Attributes
==========
* :attr:`~BaseBPoint.type` The type of the bPoint. Either ``corner`` or ``curve``.

Points
======
* :attr:`~BaseBPoint.anchor` The position of the (oncurve) anchor point.
* :attr:`~BaseBPoint.bcpIn` The position of the incoming (offcurve) bezier control point.
* :attr:`~BaseBPoint.bcpOut` The position of the outgoing (offcurve) bezier control point.

Transformations
===============
* :meth:`~BaseBPoint.transformBy` Transform the bPoint with a transformation matrix.
* :meth:`~BaseBPoint.moveBy` Move the bPoint.
* :meth:`~BaseBPoint.scaleBy` Scale the bPoint.
* :meth:`~BaseBPoint.rotateBy` Rotate the bPoint.
* :meth:`~BaseBPoint.skewBy` Skew the bPoint.

Normalization
=============
* :meth:`~BaseBPoint.round` Round the bPoint.

Environment
===========
* :meth:`~BaseBPoint.naked` Get the environment's native bPoint object.
* :meth:`~BaseBPoint.changed` Inform the environment to update the bPoint.

*********
Reference
*********

.. autoclass:: BaseBPoint

	.. autoattribute:: BaseBPoint.anchor
	.. autoattribute:: BaseBPoint.bcpIn
	.. autoattribute:: BaseBPoint.bcpOut
	.. autoattribute:: BaseBPoint.contour
	.. autoattribute:: BaseBPoint.font
	.. autoattribute:: BaseBPoint.glyph
	.. autoattribute:: BaseBPoint.index
	.. autoattribute:: BaseBPoint.layer
	.. autoattribute:: BaseBPoint.type
	.. automethod:: BaseBPoint.moveBy
	.. automethod:: BaseBPoint.naked
	.. automethod:: BaseBPoint.rotateBy
	.. automethod:: BaseBPoint.round
	.. automethod:: BaseBPoint.scaleBy
	.. automethod:: BaseBPoint.skewBy
	.. automethod:: BaseBPoint.transformBy
	.. automethod:: BaseBPoint.changed