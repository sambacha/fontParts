class Color(tuple):

    def _get_r(self):
        return _stringToSequence(self)[0]

    r = property(_get_r, "The red component.")

    def _get_g(self):
        return _stringToSequence(self)[1]

    g = property(_get_g, "The green component.")

    def _get_b(self):
        return _stringToSequence(self)[2]

    b = property(_get_b, "The blue component.")

    def _get_a(self):
        return _stringToSequence(self)[3]

    a = property(_get_a, "The alpha component.")
