import weakref
from base import BaseDict

class Groups(BaseDict):

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        This is a backwards compatibility method.
        """
        return self.font

    # Font

    _font = None

    font = dynamicProperty("font", "The groups' parent font.")

    def _get_font(self):
        if self._font is None:
            return None
        return self._font()

    def _set_font(self, font):
        assert self._font is None
        if font is not None:
            font = weakref.ref(font)
        self._font = font

	# ---------
	# Searching
	# ---------

    def findGlyph(self, glyphName):
        """
        Return a list of all groups contianing glyphName.
        """
