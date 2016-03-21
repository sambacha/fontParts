import weakref
from errors import FontPartsError
from base import BaseDict, dynamicProperty
import validators


class BaseKerning(BaseDict):

    keyValidator = validators.validateKerningKey
    valueValidator = validators.validateKerningValue

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

    font = dynamicProperty("font", "The kerning's parent font.")

    def _get_font(self):
        if self._font is None:
            return None
        return self._font()

    def _set_font(self, font):
        assert self._font is None
        if font is not None:
            font = weakref.ref(font)
        self._font = font

    # --------------
    # Transformation
    # --------------

    def scaleBy(self, value):
        """
        Scale all kernng pairs by value.
        """
        value = validators.validateTransformationScale(value)
        self._scale(value)

    def _scale(self, value):
        """
        Subclasses may override this method.
        """
        value = value[0]
        for k, v in self.items():
            v *= value
            self[key] = v

    # -------------
    # Normalization
    # -------------

    def round(self, multiple=1):
        """
        Round the kerning pair values to increments of multiple.
        """
        if not isinstance(multiple, int):
            raise FontPartsError("The round multiple must be an int not %s." % multiple.__class__.__name__)
        self._round(multiple)

    def _round(self, multiple=1):
        """
        Subclasses may override this method.
        """
        for pair, value in self.items():
            value = int(round(value / float(multiple))) * multiple
            self[pair] = value

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, minKerning, maxKerning, value, clearExisting=True):
        """
        Interpolate all pairs between minKerning and maxKerning.
        The interpolation occurs on a 0 to 1.0 range where minKerning
        is located at 0 and maxKerning is located at 1.0.

        factor is the interpolation value. It may be less than 0
        and greater than 1.0.

        clearExisting will clear existing kerning before interpolating.
        """

    # ---------------------
    # RoboFab Compatibility
    # ---------------------

    def remove(self, key):
        del self[key]

    def asDict(self):
        d = {}
        for k, v in self.items():
            d[k] = v
        return d
