import weakref
from base import BaseObject, dynamicProperty

class BaseFeatures(BaseObject):

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

    font = dynamicProperty("font", "The features' parent font.")

    def _get_font(self):
        if self._font is None:
            return None
        return self._font()

    def _set_font(self, font):
        assert self._font is None
        if font is not None:
            font = weakref.ref(font)
        self._font = font

	# ----
	# Text
	# ----

    text = dynamicProperty("text", ".fea formatted text representing the features.")

    def _get_text(self):
        self.raiseNotImplementedError()

    def _set_text(self, value):
        self.raiseNotImplementedError()
