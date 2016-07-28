.. highlight:: python
.. module:: fontParts.base

######
Groups
######

********
Overview
********
Groups are collections of glyphs. Groups are used for many things, from OpenType features, kerning, or just keeping track of a collection of related glyphs. The name of the group must be at least one character, with no limit to the maximum length for the name, nor any limit on the characters used in a name. With the exception of the kerning groups defined below, glyphs may be in more than one group and they may appear within the same group more than once. Glyphs in the groups are not required to be in the font.

Kerning Groups
==============
Groups may be used as members of kerning pairs in :class;`BaseKerning`. These groups are divided into two types: groups that appear on the first side of a kerning pair and groups that appear on the second side of a kerning pair.

Kerning groups must begin with standard prefixes. The prefix for groups intended for use in the first side of a kerning pair is “public.kern1.”. The prefix for groups intended for use in the second side of a kerning pair is “public.kern2.”. One or more characters must follow the prefix.

Kerning groups must strictly adhere to the following rules.

#. Kerning group names must begin with the appropriate prefix.
#. Only kerning groups are allowed to use the kerning group prefixes in their names.
#. Kerning groups are not required to appear in the kerning pairs.
#. Glyphs must not appear in more than one kerning group per side.

These rules come from the `Unified Font Object <http://unifiedfontobject.org/versions/ufo3/groups.plist/>`_, more information on implementation details for application developers can be found there.

::
	font = CurrentFont()
	groups = font.groups
	for name, members in groups.keys():
	    print name
	    print members

Copy
====
* :meth:`~BaseGroups.copy` Copy the groups.

Parents
=======
* :attr:`~BaseGroups.font` The groups' parent :class:`BaseFont`.

Dictionary
==========
* :meth:`~BaseGroups.__contains__` Determine if a particular group name is in the groups.
* :meth:`~BaseGroups.__delitem__` Remove a group from groups.
* :meth:`~BaseGroups.__getitem__` Get a particular group's members from the groups.
* :meth:`~BaseGroups.__iter__` Iterate over each group in the groups.
* :meth:`~BaseGroups.__len__` The number of groups.
* :meth:`~BaseGroups.__setitem__` Set a group's members.
* :meth:`~BaseGroups.clear` Remove all groups from the groups.
* :meth:`~BaseGroups.get` Get a particular group's members from the groups.
* :meth:`~BaseGroups.items` A list of each groups' members.
* :meth:`~BaseGroups.keys` The names of each group in the groups.
* :meth:`~BaseGroups.pop` Get a particular group's members from the groups and remove that group from the groups.
* :meth:`~BaseGroups.update` Update the groups.
* :meth:`~BaseGroups.values` A list of each group name and group members in the groups.

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