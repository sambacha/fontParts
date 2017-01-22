.. highlight:: python
.. module:: fontParts.base

#########
Guideline
#########

Guidelines are reference lines in a glyph that are not part of a contour or the generated font data. They are defined by a point and an angle; the guideline extends from the point in both directions on the specified angle. They are most often used to keep track of design information for a font ('my overshoots should be here') or to measure positions in a glyph ('line the ends of my serifs on this line'). They can also be used as reference positions for doing things like assembling components. In most font editors, guidelines have a special appearance and can be edited.

::

	glyph = CurrentGlyph()
	for guideline in glyph.guidelines:
	    print guideline

.. autoclass:: BaseGuideline

Copy
====

.. automethod:: BaseGuideline.copy

Parents
=======

.. autoattribute:: BaseGuideline.glyph
.. autoattribute:: BaseGuideline.layer
.. autoattribute:: BaseGuideline.font

Identification
==============

.. autoattribute:: BaseGuideline.name
.. autoattribute:: BaseGuideline.color
.. autoattribute:: BaseGuideline.identifier
.. autoattribute:: BaseGuideline.index

Attributes
==========

.. autoattribute:: BaseGuideline.x
.. autoattribute:: BaseGuideline.y
.. autoattribute:: BaseGuideline.angle

Transformations
===============

.. automethod:: BaseGuideline.transformBy
.. automethod:: BaseGuideline.moveBy
.. automethod:: BaseGuideline.scaleBy
.. automethod:: BaseGuideline.rotateBy
.. automethod:: BaseGuideline.skewBy

Normalization
=============

.. automethod:: BaseGuideline.round

Environment
===========

.. automethod:: BaseGuideline.naked
.. automethod:: BaseGuideline.changed
