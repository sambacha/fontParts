class FontPartsError(Exception): pass


class BaseObject(object):
    """
    A base object for everything.
    I'm not sure how this will work with subclassing.
    """

    def raiseNotImplementedError(self):
        """
        This exception needs to be raised frequently by
        the base classes. So, it's here for convenience.
        """
        raise FontPartsError("The {className} subclass does not implement this method.".format(className=self.__class__.__name))

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

    def getParent(self):
        """
        - this is not sufficient anymore
        """

    # ----
    # Math
    # ----

    def __mul__(self, factor):
        pass

    __rmul__ = __mul__

    def __div__(self, factor):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


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
    """

    __slots__ = [
        "name",
        "doc",
        "getterName",
        "setterName"
    ]

    def __init__(self, name, doc=None):
        self.name = name
        self.doc = doc
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
