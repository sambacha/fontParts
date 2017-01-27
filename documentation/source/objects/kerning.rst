.. highlight:: python
.. module:: fontParts.base

#######
Kerning
#######

Kerning represents the kerning data of a font. It behaves like a Python dictionary with the key being the kerning pair and the value being the kerning value. Kerning pairs can contain :class:`BaseGroups` or glyph names. If the Kerning uses :class:`BaseGroups`, the group names must follow the rules for kerning groups.

::

    font = CurrentFont()
    for pair, value in font.kerning.keys():
        print pair
        print value

It is important to understand that any changes to the returned kerning
will not be reflected in the kerning object. This means that the following will not update the font's kerning:

::

    kerning = font.kerning
    for pair in kerning:
        kerning[pair] += 10

If one wants to make a change to the kerning, one should do the following instead:

::

    kerning = font.kerning
    for pair in kerning:
        kerning[pair] = kerning[pair] + 10
    font.kerning.update(kerning)

If one wants to update the kerning for a pair, this will directly update the font's kerning, without needing to use the :meth:`BaseKerning.update` method.

::

    font.kerning[pair] = 10

.. note:: It is important to note that :class:`BaseFeatures` may contain data that is a duplicate of or data that is in conflict with the data in Kerning. Synchronization is up to the user and application developers.

.. autoclass:: BaseKerning

Copy
====

.. automethod:: BaseKerning.copy

Parents
=======

.. autoattribute:: BaseKerning.font

Dictionary
==========

.. automethod:: BaseKerning.__len__
.. automethod:: BaseKerning.keys
.. automethod:: BaseKerning.items
.. automethod:: BaseKerning.values
.. automethod:: BaseKerning.__contains__
.. automethod:: BaseKerning.__setitem__
.. automethod:: BaseKerning.__getitem__
.. automethod:: BaseKerning.get
.. automethod:: BaseKerning.__delitem__
.. automethod:: BaseKerning.pop
.. automethod:: BaseKerning.__iter__
.. automethod:: BaseKerning.update
.. automethod:: BaseKerning.clear

Transformations
===============

.. automethod:: BaseKerning.scaleBy

Interpolation
=============

.. automethod:: BaseKerning.interpolate

Normalization
=============

.. automethod:: BaseKerning.round

Environment
===========

.. automethod:: BaseKerning.naked
.. automethod:: BaseKerning.changed
