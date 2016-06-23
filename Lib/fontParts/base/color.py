class Color(tuple):

    """
    An color object. This follows the :ref:`type-color`.
    """

    def _get_r(self):
        return _stringToSequence(self)[0]

    r = property(_get_r, "The color's red component as :ref:`type-int-float`.")

    def _get_g(self):
        return _stringToSequence(self)[1]

    g = property(_get_g, "The color's green component as :ref:`type-int-float`.")

    def _get_b(self):
        return _stringToSequence(self)[2]

    b = property(_get_b, "The color's blue component as :ref:`type-int-float`.")

    def _get_a(self):
        return _stringToSequence(self)[3]

    a = property(_get_a, "The color's alpha component as :ref:`type-int-float`.")

    def _stringToSequence(value):
        r, g, b, a = [i.strip() for i in value.split(",")]
        value = []
        for component in (r, g, b, a):
            try:
                v = int(component)
                value.append(v)
                continue
            except ValueError:
                pass
            v = float(component)
            value.append(v)
        return value
