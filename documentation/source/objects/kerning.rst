.. highlight:: python
.. module:: fontParts.base

#######
Kerning
#######

********
Overview
********

Copy
====
* :meth:`~BaseKerning.copy` Copy the kerning.

Parents
=======
* :attr:`~BaseKerning.font` The kerning's parent :class:`BaseFont`.

Dictionary
==========
* :meth:`~BaseKerning.__len__` The number of kerning pairs.
* :meth:`~BaseKerning.keys` Get a ``list`` of all kerning pairs.
* :meth:`~BaseKerning.items` Get a ``list`` of all kerning pairs and their value.
* :meth:`~BaseKerning.values` Get a ``list`` of all kerning values.
* :meth:`~BaseKerning.__contains__` Determine if a kerning pair is in the kerning.
* :meth:`~BaseKerning.__setitem__` Set the value of a kerning pair.
* :meth:`~BaseKerning.__getitem__` Get the value of a kerning pair.
* :meth:`~BaseKerning.get` Get the value of a kerning pair.
* :meth:`~BaseKerning.__delitem__` Remove a kerning pair.
* :meth:`~BaseKerning.pop` Get a kerning value for a pair and remove that pair from the kerning.
* :meth:`~BaseKerning.__iter__` Iterate over each kerning pair.
* :meth:`~BaseKerning.update` Update Kerning with a ``dict`` of kerning information.
* :meth:`~BaseKerning.clear` Removes all kerning from the font.

Transformations
===============
* :meth:`~BaseKerning.scaleBy` Scale the kerning by a value.

Interpolation
=============
* :meth:`~BaseKerning.interpolate` Interpolate between two sets of Kerning objects by a factor.

Normalization
=============
* :meth:`~BaseKerning.round` Round the kerning by a specified increment.

Environment
===========
* :meth:`~BaseKerning.naked` Get the environment's native Kerning object.
* :meth:`~BaseKerning.update` Inform the environment to update the kerning.


*********
Reference
*********

.. autoclass:: BaseKerning

    .. autoattribute:: BaseKerning.font
    .. automethod:: BaseKerning.__contains__
    .. automethod:: BaseKerning.__delitem__
    .. automethod:: BaseKerning.__getitem__
    .. automethod:: BaseKerning.__iter__
    .. automethod:: BaseKerning.__len__
    .. automethod:: BaseKerning.__setitem__
    .. automethod:: BaseKerning.clear
    .. automethod:: BaseKerning.copy
    .. automethod:: BaseKerning.get
    .. automethod:: BaseKerning.interpolate
    .. automethod:: BaseKerning.items
    .. automethod:: BaseKerning.keys
    .. automethod:: BaseKerning.naked
    .. automethod:: BaseKerning.pop
    .. automethod:: BaseKerning.round    
    .. automethod:: BaseKerning.scaleBy
    .. automethod:: BaseKerning.update
    .. automethod:: BaseKerning.update
    .. automethod:: BaseKerning.values