.. highlight:: python
.. module:: fontParts.base

#####
Layer
#####

.. note::

	This section needs to contain the following:

	* description of what this is
	* sub-object with basic usage
	* glyph interaction with basic usage

.. autoclass:: BaseLayer

Copy
====

.. automethod:: BaseLayer.copy

Parents
=======

.. autoattribute:: BaseLayer.font

Attributes
==========

.. autoattribute:: BaseLayer.name
.. autoattribute:: BaseLayer.color

Sub-Objects
===========

.. autoattribute:: BaseLayer.lib

Glyphs
======

.. automethod:: BaseLayer.__len__
.. automethod:: BaseLayer.keys
.. automethod:: BaseLayer.__iter__
.. automethod:: BaseLayer.__contains__
.. automethod:: BaseLayer.__getitem__
.. automethod:: BaseLayer.newGlyph
.. automethod:: BaseLayer.insertGlyph
.. automethod:: BaseLayer.removeGlyph

Interpolation
=============

.. automethod:: BaseLayer.isCompatible
.. automethod:: BaseLayer.interpolate

Normalization
=============

.. automethod:: BaseLayer.round
.. automethod:: BaseLayer.autoUnicodes

Environment
===========

.. automethod:: BaseLayer.naked
.. automethod:: BaseLayer.changed
