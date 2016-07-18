.. highlight:: python
.. module:: fontParts.base

######
Groups
######

********
Overview
********

Copy
====
* :meth:`~BaseGroups.copy` Copy the groups.

Parents
=======
* :attr:`~BaseGroups.font` The groups' parent :class:`BaseFont`.

Dictionary
==========
* :meth:`~BaseGroups.__len__` The number of groups.
* :meth:`~BaseGroups.keys` The names of each group in the groups.
* :meth:`~BaseGroups.items` A list of each groups' members.
* :meth:`~BaseGroups.values` A list of each group name and group members in the groups.
* :meth:`~BaseGroups.__contains__` Determine if a particular group name is in the groups.
* :meth:`~BaseGroups.__setitem__` Set a group's members.
* :meth:`~BaseGroups.__getitem__` Get a particular group's members from the groups.
* :meth:`~BaseGroups.get` Get a particular group's members from the groups.
* :meth:`~BaseGroups.__delitem__` Remove a group from groups.
* :meth:`~BaseGroups.pop` Get a particular group's members from the groups and remove that group from the groups.
* :meth:`~BaseGroups.__iter__` Iterate over each group in the groups.
* :meth:`~BaseGroups.update` Update the groups.
* :meth:`~BaseGroups.clear` Remove all groups from the groups.

Queries
=======
* :meth:`~BaseGroups.findGlyph` Find all groups that contain a given glyph.

Environment
===========
* :meth:`~BaseGroups.naked` Get the environment's native groups object.
* :meth:`~BaseGroups.update` Inform the environment to update the groups.


*********
Reference
*********

.. autoclass:: BaseGroups

	.. autoattribute:: BaseGroups.font
	.. automethod:: BaseGroups.__contains__
	.. automethod:: BaseGroups.__delitem__
	.. automethod:: BaseGroups.__getitem__
	.. automethod:: BaseGroups.__iter__
	.. automethod:: BaseGroups.__len__
	.. automethod:: BaseGroups.__setitem__
	.. automethod:: BaseGroups.clear
	.. automethod:: BaseGroups.copy
	.. automethod:: BaseGroups.findGlyph
	.. automethod:: BaseGroups.get
	.. automethod:: BaseGroups.items
	.. automethod:: BaseGroups.keys
	.. automethod:: BaseGroups.naked
	.. automethod:: BaseGroups.pop
	.. automethod:: BaseGroups.update
	.. automethod:: BaseGroups.update
	.. automethod:: BaseGroups.values