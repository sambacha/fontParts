.. highlight:: python

###########
Documenting
###########

In general, follow the suggestions `here <https://docs.python.org/devguide/documenting.html>`_.

**************
Heading Levels
**************

::

    #######
    Level 1
    #######

    *******
    Level 2
    *******

    Level 3
    =======

    Level 4
    -------

    Level 5
    ^^^^^^^

    Level 6
    """""""

**********
Paragraphs
**********

::

    .. note::
    .. warning::
    .. versionadded::
    .. versionchanged::
    .. seealso::

******
Inline
******

::

    *emphasis (italics)*
    **strong (bold)**
    ``code``

*****
Links
*****

::

    `Some text <http://target>`_
    :mod:`module`
    :func:`module.functionName`
    :class:`ClassName`
    :meth:`ClassName.methodName`
    :attr:`ClassName.attribute`
    :exc:`ExceptionName`
    :ref:`my-reference-label`

*****
Lists
*****

::

    * unordered
    * list

    #. ordered
    #. list

******
Tables
******

::

    +---------+--------------+
    | option1 | Description. |
    +---------+--------------+
    | option2 | Description. |
    +---------+--------------+

*******
Objects
*******

In the public methods that will generate API reference, use as little technical jargon as possible. In the environment implementation methods, be very thorough.

Properties
==========

::

    something = dynamicProperty(
        "something",
        """
        The something.

            >>> something = something.something
        """
    )

Functions/Methods
=================

::

    def something(arg, kwarg="blah"):
        """
        **arg** This is the description for arg.

            * what it means/does
            * the options
            * valid/invalid types/values
            * the default

        If there are set options, use a table.
        """

    path = dynamicProperty(
        "base_path",
        """
        The path to the file this object represents.

            >>> print font.path
            "/path/to/my/font.ufo"
        """
    )

Examples
========

Not everything needs an example. When they are needed, keep them concise and generic and provide a clear description. ::

    """
    Returns the contents of the named group.

        >>> font.groups["myGroup"]
        ["A", "B", "C"]

    The returned list is immutable.
    """

Stock Statements
================

* This attribute is read only.
* Subclasses must override this method.
* Subclasses may override this method.
