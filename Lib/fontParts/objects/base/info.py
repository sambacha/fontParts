import weakref
from ufoLib import fontInfoAttributesVersion3, validateFontInfoVersion3ValueForAttribute
from errors import FontPartsError
from base import BaseObject, dynamicProperty

_copyAttributes = fontInfoAttributesVersion3
_copyAttributes.remove("guidelines")
_copyAttributes = tuple(_copyAttributes)


class BaseInfo(BaseObject):

    copyAttributes = _copyAttributes

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

    font = dynamicProperty("font", "The info's parent font.")

    def _get_font(self):
        if self._font is None:
            return None
        return self._font()

    def _set_font(self, font):
        assert self._font is None
        if font is not None:
            font = weakref.ref(font)
        self._font = font

    # ----------
    # Validation
    # ----------

    def _validateFontInfoAttributeValue(self, attr, value):
        valid = validateFontInfoVersion3ValueForAttribute(attr, value)
        if not valid:
            raise FontPartsError("Invalid value %s for attribute '%s'." % (value, attr))
        return value

    # ----------
    # Attributes
    # ----------

    # has

    def __hasattr__(self, attr):
        if attr in fontInfoAttributesVersion3:
            return True
        return super(BaseInfo, self).__hasattr__(attr)

    # get

    def __getattr__(self, attr):
        if attr != "guidelines" and attr in fontInfoAttributesVersion3:
            value = self._getAttr(attr)
            if value is not None:
                value = self._validateFontInfoAttributeValue(attr, value)
            return value
        return super(BaseInfo, self).__getattr__(attr)

    def _getAttr(self, attr):
        """
        Subclasses may override this method.

        If a subclass does not override this method,
        it must implement '_get_attributeName' methods
        for all Info methods.
        """
        meth = "_get_%s" % attr
        if not hasattr(self, meth):
            raise AttributeError("No getter for attribute '%s'." % attr)
        meth = getattr(self, meth)
        value = meth()
        return value

    # set

    def __setattr__(self, attr, value):
        if attr != "guidelines" and attr in fontInfoAttributesVersion3:
            if value is not None:
                value = self._validateFontInfoAttributeValue(attr, value)
            return self._setAttr(attr, value)
        return super(BaseInfo, self).__setattr__(attr, value)

    def _setAttr(self, attr, value):
        """
        Subclasses may override this method.

        If a subclass does not override this method,
        it must implement '_set_attributeName' methods
        for all Info methods.
        """
        meth = "_set_%s" % attr
        if not hasattr(self, meth):
            raise AttributeError("No setter for attribute '%s'." % attr)
        meth = getattr(self, meth)
        meth(value)
