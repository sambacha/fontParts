class RBaseObject(object):

    def naked(self):
        return self._wrapped

    def _convertFromDefconColor(self, value):
        return [i for i in value]