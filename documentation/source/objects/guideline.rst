.. highlight:: python
.. module:: fontParts.base

#########
Guideline
#########

********
Overview
********

Guidelines are reference lines in a glyph that are not part of a contour or the generated font data. They are defined by a point and an angle; the guideline extends from the point in both directions on the specified angle. They are most often used to keep track of design information for a font ('my overshoots should be here') or to measure positions in a glyph ('line the ends of my serifs on this line'). They can also be used as reference positions for doing things like assembling components. In most font editors, guidelines have a special appearance and can be edited.

::

	glyph = CurrentGlyph()
	for guideline in glyph.guidelines:
	    print guideline

Copy
====
* :meth:`~BaseGuideline.copy` Copy the guideline.

Parents
=======
* :attr:`~BaseGuideline.glyph` The guideline's parent :class:`BaseGlyph`.
* :attr:`~BaseGuideline.layer` The guideline's parent :class:`BaseLayer`.
* :attr:`~BaseGuideline.font` The guideline's parent :class:`BaseFont`.

Identification
==============
* :attr:`~BaseGuideline.name` The name of the guideline.
* :attr:`~BaseGuideline.color` The color of the guideline.
* :attr:`~BaseGuideline.identifier` The identifier of the guideline.
* :attr:`~BaseGuideline.index` The index of the guideline within the parent glyph's ordered list of anchors.

Attributes
==========
* :attr:`~BaseGuideline.x` The x position of the guideline.
* :attr:`~BaseGuideline.y` The y position of the guideline.
* :attr:`~BaseGuideline.angle` The angle of the guideline.

Transformations
===============
* :meth:`~BaseGuideline.transformBy` Transform the guideline with a transformation matrix.
* :meth:`~BaseGuideline.moveBy` Move the guideline.
* :meth:`~BaseGuideline.scaleBy` Scale the guideline.
* :meth:`~BaseGuideline.rotateBy` Rotate the guideline.
* :meth:`~BaseGuideline.skewBy` Skew the guideline.

Normalization
=============
* :meth:`~BaseGuideline.round` Round the guideline's x and y position. This does not round the angle value, which will be a decimal number.

Environment
===========
* :meth:`~BaseGuideline.naked` Get the environment's native guideline object.
* :meth:`~BaseGuideline.changed` Inform the environment to update the anchor.


*********
Reference
*********

.. autoclass:: BaseGuideline

	.. autoattribute:: BaseGuideline.angle
	.. autoattribute:: BaseGuideline.color
	.. autoattribute:: BaseGuideline.font
	.. autoattribute:: BaseGuideline.glyph
	.. autoattribute:: BaseGuideline.identifier
	.. autoattribute:: BaseGuideline.index
	.. autoattribute:: BaseGuideline.layer
	.. autoattribute:: BaseGuideline.name
	.. autoattribute:: BaseGuideline.x
	.. autoattribute:: BaseGuideline.y
	.. automethod:: BaseGuideline.copy
	.. automethod:: BaseGuideline.moveBy
	.. automethod:: BaseGuideline.naked
	.. automethod:: BaseGuideline.rotateBy
	.. automethod:: BaseGuideline.round	
	.. automethod:: BaseGuideline.scaleBy
	.. automethod:: BaseGuideline.skewBy
	.. automethod:: BaseGuideline.transformBy
	.. automethod:: BaseGuideline.changed