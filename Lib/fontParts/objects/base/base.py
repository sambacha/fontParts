import math
from fontTools.misc import transform
from errors import FontPartsError
import validators

# ------------
# Base Objects
# ------------

class BaseObject(object):

    # --------------
    # Initialization
    # --------------

    def __init__(self, *args, **kwargs):
        self._init(*args, **kwargs)

    def _init(self, *args, **kwargs):
        """
        Subclasses may override this method.
        """
        pass

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


class TransformationMixin(object):

    # ---------------
    # Transformations
    # ---------------

    def transformBy(self, matrix, origin=None):
        """
        Transform the object with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.

        origin, (x, y) or None, defines the point at which the
        transformation should orginate. The default is (0, 0).
        """
        matrix = validators.validateTransformationMatrix(matrix)
        if origin is None:
            origin = (0, 0)
        origin = validators.validateCoordinateTuple(origin)
        # calculate the origin offset
        if origin == (0, 0):
            originOffset = (0, 0)
        else:
            t = transform.Transform(*matrix)
            bx, by = origin
            ax, ay = t.transformPoint((bx, by))
            originOffset = (bx - ax, by - ay)
        # apply
        self._transformBy(matrix, origin=origin, originOffset=originOffset)

    def _transformBy(self, matrix, origin=None, originOffset=None, **kwargs):
        """
        Transform the object with the matrix.
        The matrix will be a tuple of floats defining a 2x2
        transformation plus offset, aka Affine transform.
        origin will be a coordinate tuple (x, y).
        originOffset will be a precalculated offset (x, y)
        that represents the delta necessary to realign
        the post-transformation origin point with the
        pre-transformation point.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def moveBy(self, value):
        """
        Move the object by value. Value must
        be a tuple defining x and y values.
        """
        value = validators.validateTransformationOffset(value)
        self._moveBy(value)

    def _moveBy(self, value, **kwargs):
        """
        Move the object by value.
        The value will be a tuple of (x, y) where
        x and y are ints or floats.

        Subclasses may override this method.
        """
        x, y = value
        t = transform.Offset(x, y)
        self.transformBy(tuple(t))

    def scaleBy(self, value, origin=None):
        """
        Scale the object by value. value must be a
        tuple defining x and y values or a number.

        origin, (x, y) or None, defines the point at which the
        transformation should orginate. The default is (0, 0).
        """
        value = validators.validateTransformationScale(value)
        if origin is None:
            origin = (0, 0)
        origin = validators.validateCoordinateTuple(origin)
        self._scaleBy(value, origin=origin)

    def _scaleBy(self, value, origin=None, **kwargs):
        """
        Scale the object by value.
        The value will be a tuple of x, y factors.
        origin will be a coordinate tuple (x, y).

        Subclasses may override this method.
        """
        x, y = value
        t = transform.Identity.scale(x=x, y=y)
        self.transformBy(tuple(t), origin=origin)

    def rotateBy(self, value, origin=None):
        """
        Rotate the object by value.

        origin, (x, y) or None, defines the point at which the
        transformation should orginate. The default is (0, 0).
        """
        value = validators.validateTransformationRotationAngle(value)
        if origin is None:
            origin = (0, 0)
        origin = validators.validateCoordinateTuple(origin)
        self._rotateBy(value, origin=origin)

    def _rotateBy(self, value, origin=None, **kwargs):
        """
        Rotate the object by value.
        The value will be a float between 0 and 360 degrees.
        origin will be a coordinate tuple (x, y).

        Subclasses may override this method.
        """
        a = math.radians(value)
        t = transform.Identity.rotate(a)
        self.transformBy(tuple(t), origin=origin)

    def skewBy(self, value, origin=None):
        """
        Skew the object by value. value can be a single
        number indicating an x skew or a tuple indicating an
        x, y skew.

        origin, (x, y) or None, defines the point at which the
        transformation should orginate. The default is (0, 0).
        """
        value = validators.validateTransformationSkewAngle(value)
        if origin is None:
            origin = (0, 0)
        origin = validators.validateCoordinateTuple(origin)
        self._skewBy(value, origin=origin)

    def _skewBy(self, value, origin=None, **kwargs):
        """
        Rotate the object by value.
        The value will be a tuple of two angles between
        0 and 360 degrees.
        origin will be a coordinate tuple (x, y).

        Subclasses may override this method.
        """
        x, y = value
        x = math.radians(x)
        y = math.radians(y)
        t = transform.Identity.skew(x=x, y=y)
        self.transformBy(tuple(t), origin=origin)


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
