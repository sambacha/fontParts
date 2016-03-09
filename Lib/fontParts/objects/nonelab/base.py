class RBaseObject(object):

    def __eq__(self, other):
        if hasattr(other, "_wrapped"):
            return self._wrapped == other._wrapped
        return False

    def naked(self):
        return self._wrapped

    def _convertFromDefconColor(self, value):
        return [i for i in value]