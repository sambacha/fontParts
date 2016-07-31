.. highlight:: python
.. module:: fontParts.base

######
Groups
######

********
Overview
********
Groups are collections of glyphs. Groups are used for many things, from OpenType features, kerning, or just keeping track of a collection of related glyphs. The name of the group must be at least one character, with no limit to the maximum length for the name, nor any limit on the characters used in a name. With the exception of the kerning groups defined below, glyphs may be in more than one group and they may appear within the same group more than once. Glyphs in the groups are not required to be in the font.

Groups behave like a Python dictionary. Anything you can do with a dictionary in Python, you can do with Groups.

::

    font = CurrentFont()
    for name, members in font.groups.keys():
        print name
        print members

It is important to understand that any changes to the returned group contents 
will not be reflected in the groups object. This means that the following will not update the font's groups.

::

    group = font.groups["myGroup"]
    group.remove("A")

If one wants to make a change to the group contents, one should do the following instead.

::

    group = font.groups["myGroup"]
    group.remove("A")
    font.groups["myGroup"] = group

Kerning Groups
--------------
Groups may be used as members of kerning pairs in :class:`BaseKerning`. These groups are divided into two types: groups that appear on the first side of a kerning pair and groups that appear on the second side of a kerning pair.

Kerning groups must begin with standard prefixes. The prefix for groups intended for use in the first side of a kerning pair is “public.kern1.”. The prefix for groups intended for use in the second side of a kerning pair is “public.kern2.”. One or more characters must follow the prefix.

Kerning groups must strictly adhere to the following rules.

#. Kerning group names must begin with the appropriate prefix.
#. Only kerning groups are allowed to use the kerning group prefixes in their names.
#. Kerning groups are not required to appear in the kerning pairs.
#. Glyphs must not appear in more than one kerning group per side.

These rules come from the `Unified Font Object <http://unifiedfontobject.org/versions/ufo3/groups.plist/>`_, more information on implementation details for application developers can be found there.

Copy
====
* :meth:`~BaseGroups.copy` Copy the groups.

Parents
=======
* :attr:`~BaseGroups.font` The groups' parent :class:`BaseFont`.

Dictionary
==========
* :meth:`~BaseGroups.__contains__` Determine if a particular group name is in the Groups.
* :meth:`~BaseGroups.__delitem__` Remove a group from Groups.
* :meth:`~BaseGroups.__getitem__` Get a particular group's members from the Groups.
* :meth:`~BaseGroups.__iter__` Iterate over each group in the Groups.
* :meth:`~BaseGroups.__len__` The number of Groups.
* :meth:`~BaseGroups.__setitem__` Set a group's members.
* :meth:`~BaseGroups.clear` Remove all groups from the Groups.
* :meth:`~BaseGroups.get` Get a particular group's members from the Groups.
* :meth:`~BaseGroups.items` A list of each group name and group members in the Groups.
* :meth:`~BaseGroups.keys` The names of each group in the Groups.
* :meth:`~BaseGroups.pop` Get a particular group's members from the Groups and remove that group from the Groups.
* :meth:`~BaseGroups.update` Update Groups with ``dict`` of group information.
* :meth:`~BaseGroups.values` A list of each groups' members.

Queries
=======
* :meth:`~BaseGroups.findGlyph` Find all groups that contain a given glyph.

Environment
===========
* :meth:`~BaseGroups.naked` Get the environment's native Groups object.
* :meth:`~BaseGroups.changed` Inform the environment to update the Groups.


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
    .. automethod:: BaseGroups.values
    .. automethod:: BaseGroups.changed