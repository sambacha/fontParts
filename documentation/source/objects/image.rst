.. highlight:: python
.. module:: fontParts.base

#####
Image
#####

********
Overview
********

Copy
====
* :meth:`~BaseImage.copy` Copy the image.

Parents
=======
* :attr:`~BaseImage.glyph` The image's parent :class:`BaseGlyph`.
* :attr:`~BaseImage.layer` The image's parent :class:`BaseLayer`.
* :attr:`~BaseImage.font` The image's parent :class:`BaseFont`.

Attributes
==========
* :attr:`~BaseImage.data` (add general description)
* :attr:`~BaseImage.color` (add general description)
* :attr:`~BaseImage.transformation` (add general description)
* :attr:`~BaseImage.offset` (add general description)
* :attr:`~BaseImage.scale` (add general description)

Transformations
===============
* :meth:`~BaseImage.transformBy` Transform the image with a transformation matrix.
* :meth:`~BaseImage.moveBy` Move the image.
* :meth:`~BaseImage.scaleBy` Scale the image.
* :meth:`~BaseImage.rotateBy` Rotate the image.
* :meth:`~BaseImage.skewBy` Skew the image.

Normalization
=============
* :meth:`~BaseImage.round` Round the image.

Environment
===========
* :meth:`~BaseImage.naked` Get the environment's native image object.
* :meth:`~BaseImage.changed` Inform the environment to update the image.


*********
Reference
*********

.. autoclass:: BaseImage

	.. autoattribute:: BaseImage.color
	.. autoattribute:: BaseImage.data
	.. autoattribute:: BaseImage.font
	.. autoattribute:: BaseImage.glyph
	.. autoattribute:: BaseImage.layer
	.. autoattribute:: BaseImage.offset
	.. autoattribute:: BaseImage.scale
	.. autoattribute:: BaseImage.transformation
	.. automethod:: BaseImage.copy
	.. automethod:: BaseImage.moveBy
	.. automethod:: BaseImage.naked
	.. automethod:: BaseImage.rotateBy
	.. automethod:: BaseImage.round
	.. automethod:: BaseImage.scaleBy
	.. automethod:: BaseImage.skewBy
	.. automethod:: BaseImage.transformBy
	.. automethod:: BaseImage.changed