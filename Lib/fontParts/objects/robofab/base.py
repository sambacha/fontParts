class BaseObject(object):
    """
    A base object for everything.
    I'm not sure how this will work with subclassing.
    """

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