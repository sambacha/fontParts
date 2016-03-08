# -------------------
# Universal Exception
# -------------------

class FontPartsError(Exception): pass


# ------------
# Base Objects
# ------------

class BaseObject(object):

    # ----
    # Copy
    # ----

    copyClass = None
    copyAttributes = ()

    def copy(self):
        copyClass = self.copyClass
        if copyClass is None:
            copyClass = self.__class__
        copied = copyClass()
        for attr in self.copyAttributes:
            v = getattr(self, attr)
            setattr(copied, attr, v)
        return copied

    # ----------
    # Exceptions
    # ----------

    def raiseNotImplementedError(self):
        """
        This exception needs to be raised frequently by
        the base classes. So, it's here for convenience.
        """
        raise FontPartsError("The {className} subclass does not implement this method.".format(className=self.__class__.__name__))

    # ---------------------
    # Environment Fallbacks
    # ---------------------

    def update(self):
        """
        Tell the environment that something has changed in
        the object. The behavior of this method will vary
        from environment to environment.
        """

    def naked(self):
        """
        Return the wrapped object itself, in case it is needed for direct access.
        """
        self.raiseNotImplementedError()

    # ----
    # Math
    # ----

    def __mul__(self, factor):
        self.raiseNotImplementedError()

    __rmul__ = __mul__

    def __div__(self, factor):
        self.raiseNotImplementedError()

    def __add__(self, other):
        self.raiseNotImplementedError()

    def __sub__(self, other):
        self.raiseNotImplementedError()


class BaseDict(BaseObject):

    def fromkeys(self, keys):
        self.raiseNotImplementedError()

    def len(self):
        return len(self.keys())

    def keys(self):
        return [k for k, v in self.items()]

    def items(self):
        self.raiseNotImplementedError()

    def values(self):
        return [v for k, v in self.items()]

    def __contains__(self, key):
        self.raiseNotImplementedError()

    has_key = __contains__

    def __getitem__(self, key):
        self.raiseNotImplementedError()

    def get(self, key, default=None):
        if key in self:
            return self[key]
        return default

    def __delitem__(self, key):
        self.raiseNotImplementedError()

    def pop(self, key, default=None):
        value = default
        if key in self:
            value = self[key]
            del self[key]
        return value

    def popitem(self):
        self.raiseNotImplementedError()

    def __iter__(self):
        self.raiseNotImplementedError()

    def iteritems(self):
        self.raiseNotImplementedError()

    def iterkeys(self):
        self.raiseNotImplementedError()

    def itervalues(self):
        self.raiseNotImplementedError()

    def viewitems(self):
        self.raiseNotImplementedError()

    def viewkeys(self):
        self.raiseNotImplementedError()

    def viewvalues(self):
        self.raiseNotImplementedError()

    def setdefault(self, value):
        self.raiseNotImplementedError()

    def update(self, other):
        for key, value in other.items():
            self[key] = value

    def clear(self):
        for key in self.keys():
            del self[key]

    def copy(self):
        self.raiseNotImplementedError()


# -------
# Helpers
# -------

class dynamicProperty(object):

    """
    This implements functionality that is very similar
    to Python's built in property function, but makes
    it much easier for subclassing. Here is an example
    of why this is needed:

        class BaseObject(object):

            _foo = 1

            def _get_foo(self):
                return self._foo

            def _set_foo(self, value):
                self._foo = value

            foo = property(_get_foo, _set_foo)


        class MyObject(BaseObject):

            def _set_foo(self, value):
                self._foo = value * 100


        >>> m = MyObject()
        >>> m.foo
        1
        >>> m.foo = 2
        >>> m.foo
        2

    The expected value is 200. The _set_foo method
    needs to be reregistered. Doing that also requires
    reregistering the _get_foo method. It's possible
    to do this, but it's messy and will make subclassing
    less than ideal.

    Using dynamicProperty solves this.

        class BaseObject(object):

            _foo = 1

            foo = dynamicProperty("foo")

            def _get_foo(self):
                return self._foo

            def _set_foo(self, value):
                self._foo = value


        class MyObject(BaseObject):

            def _set_foo(self, value):
                self._foo = value * 100


        >>> m = MyObject()
        >>> m.foo
        1
        >>> m.foo = 2
        >>> m.foo
        200
    """

    __slots__ = [
        "name",
        "doc",
        "getterName",
        "setterName",
        "__dict__" # this is needed to enable the __doc__ setting in __init__
    ]

    def __init__(self, name, doc=None):
        self.name = name
        self.__doc__ = doc
        self.getterName = "_get_" + name
        self.setterName = "_set_" + name

    def __get__(self, obj, cls):
        getter = getattr(obj, self.getterName, None)
        if getter is not None:
            return getter()
        else:
            raise AttributeError("no getter for %r" % self.name)

    def __set__(self, obj, value):
        setter = getattr(obj, self.setterName, None)
        if setter is not None:
            setter(value)
        else:
            raise AttributeError("no setter for %r" % self.name)
