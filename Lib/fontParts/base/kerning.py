import weakref
import fontMath
from fontParts.base.errors import FontPartsError
from fontParts.base.base import BaseDict, dynamicProperty, interpolate
from fontParts.base import normalizers


class BaseKerning(BaseDict):

    keyNormalizer = normalizers.normalizeKerningKey
    valueNormalizer = normalizers.normalizeKerningValue

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
        assert self._font is None or self._font() == font
        if font is not None:
            font = weakref.ref(font)
        self._font = font

    # --------------
    # Transformation
    # --------------

    def scaleBy(self, value):
        """
        Scale all kerning pairs by value.
        """
        value = normalizers.normalizeTransformationScale(value)
        self._scale(value)

    def _scale(self, value):
        """
        Subclasses may override this method.
        """
        value = value[0]
        for k, v in self.items():
            v *= value
            self[k] = v

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
            value = int(normalizers.normalizeRounding(value / float(multiple))) * multiple
            self[pair] = value

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minKerning, maxKerning, round=True, suppressError=True):
        """
        Interpolate all pairs between minKerning and maxKerning.
        The interpolation occurs on a 0 to 1.0 range where minKerning
        is located at 0 and maxKerning is located at 1.0.

        factor is the interpolation value. It may be less than 0
        and greater than 1.0. It may be a number (integer, float)
        or a tuple of two numbers. If it is a tuple, the first
        number indicates the x factor and the second number
        indicates the y factor.

        round indicates if the result should be rounded to integers.

        suppressError indicates if incompatible data should be ignored
        or if an error should be raised when such incompatibilities are found.
        """
        factor = normalizers.normalizeInterpolationFactor(factor)
        if not isinstance(minKerning, BaseKerning):
            raise FontPartsError("Interpolation to an instance of %r can not be performed from an instance of %r." % (self.__class__.__name__, minKerning.__class__.__name__))
        if not isinstance(maxKerning, BaseKerning):
            raise FontPartsError("Interpolation to an instance of %r can not be performed from an instance of %r." % (self.__class__.__name__, maxKerning.__class__.__name__))
        round = normalizers.normalizeBoolean(round)
        suppressError = normalizers.normalizeBoolean(suppressError)
        self._interpolate(factor, minKerning, maxKerning, round=round, suppressError=suppressError)

    def _interpolate(self, factor, minKerning, maxKerning, round=True, suppressError=True):
        """
        Subclasses may override this method.
        """
        minKerning = fontMath.MathKerning(kerning=minKerning, groups=minKerning.font.groups)
        maxKerning = fontMath.MathKerning(kerning=maxKerning, groups=maxKerning.font.groups)
        result = interpolate(minKerning, maxKerning, factor)
        if round:
            result.round()
        self.clear()
        result.extractKerning(self.font)

    # ---------------------
    # RoboFab Compatibility
    # ---------------------

    def remove(self, key):
        del self[key]

    def asDict(self, returnIntegers=True):
        d = {}
        for k, v in self.items():
            d[k] = v if not returnIntegers else normalizers.normalizeRounding(v)
        return d

    # -------------------
    # Inherited Functions
    # -------------------
    
    def __contains__(self, pair):
        """
        Tests to see if a pair is in the Kerning. 
        **pair** will be a ``tuple`` of two :ref:`type-string`s. 
        This returns a ``bool`` indicating if the **pair**
        is in the Kerning. ::
        
            >>> ("A", "V") in font.kerning
            True
        """
        return super(BaseKerning, self).__contains__(pair)

    def __delitem__(self, pair):
        """
        Removes **pair** from the Kerning. **pair** is a ``tuple`` of two :ref:`type-string`s.::
        
            >>> del font.kerning["myGroup"]
        """
        super(BaseKerning, self).__delitem__(pair)

    def __getitem__(self, pair):
        """
        Returns the kerning value of the pair. **pair** is a ``tuple`` of two :ref:`type-string`s.
        The returned value will be a ``int``.::
        
            >>> font.kerning[("A", "V")]
            -15
            
        It is important to understand that any changes to the returned value 
        will not be reflected in the Kerning object. If one wants to make a change to 
        the value, one should do the following::
        
            >>> value = font.kerning[("A", "V")]
            >>> value += 10
            >>> font.kerning[("A", "V")] = value
        """
        return super(BaseKerning, self).__getitem__(pair)
        
    def __iter__(self):
        """
        Iterates through the Kerning, giving the pair for each iteration. The order that
        the Kerning will iterate though is not fixed nor is it ordered.::
        
            >>> for pair in font.kerning:
            >>>     print pair
            ("A", "Y")
            ("A", "V")
            ("A", "W")
        """
        return super(BaseKerning, self).__iter__()
        
    def __len__(self):
        """
        Returns the number of pairs in Kerning as an ``int``.::
        
            >>> len(font.kerning)
            5
        """
        return super(BaseKerning, self).__len__()
        
    def __setitem__(self, pair, value):
        """
        Sets the **pair** to the list of **value**. **pair** is the 
        pair as a ``tuple`` of two :ref:`type-string`s and **value** is a ``int``.
        
            >>> font.kerning[("A", "V")] = -20
        """
        super(BaseKerning, self).__setitem__(pair, value)
        
    def clear(self):
        """
        Removes all group information from Kerning, 
        resetting the Kerning to an empty dictionary. ::
        
            >>> font.kerning.clear()
        """
        super(BaseKerning, self).clear()

    def get(self, pair, default=None):
        """
        Returns the value for the kerning pair. 
        **pair** is a ``tuple`` of two :ref:`type-string`s, and the returned values will either 
        be ``int`` or ``None`` if no pair was found. ::
        
            >>> font.kerning[("A", "V")]
            -25
        
        It is important to understand that any changes to the returned value 
        will not be reflected in the Kerning object. If one wants to make a change to 
        the value, one should do the following::
        
            >>> value = font.kerning[("A", "V")]
            >>> value += 10
            >>> font.kerning[("A", "V")] = value
        """
        return super(BaseKerning, self).get(pair, default)

    def items(self):
        """
        Returns a list of ``tuple``s of each pair and value. Pairs are a
        ``tuple`` of two :ref:`type-string`s and values are ``int``.
        The initial list will be unordered.
        
            >>> font.kerning.items()
            [(("A", "V"), -30), (("A", "W"), -10)]
        """
        return super(BaseKerning, self).items()

    def keys(self):
        """
        Returns a ``list`` of all the pairs in Kerning. This list will be
        unordered.::
        
            >>> font.kerning.keys()
            [("A", "Y"), ("A", "V"), ("A", "W")]
        """
        return super(BaseKerning, self).keys()

    def pop(self, pair, default=None):
        """
        Removes the **pair** from the Kerning and returns the value as an ``int``. 
        If no pair is found, **default** is returned. **pair** is a
        ``tuple`` of two :ref:`type-string`s. This must return either 
        **default** or a ``int``.
        
            >>> font.kerning.pop(("A", "V"))
            -15
        """
        return super(BaseKerning, self).pop(pair, default)

    def update(self, otherKerning):
        """
        Updates the Kerning based on **otherKerning**. *otherKerning** is a ``dict`` of 
        kerning information. If a pair from **otherKerning** is in Kerning, the pair 
        value will be replaced by the value from **otherKerning**. If a pair 
        from **otherKerning** is not in the Kerning, it is added to the pairs. If Kerning 
        contains a pair that is not in *otherKerning**, it is not changed.
        
            >>> font.kerning.update(newKerning)
        """
        super(BaseKerning, self).update(otherKerning)

    def values(self):
        """
        Returns a ``list`` of each pair's values, the values will be ``int``s. 
        The list will be unordered.
        
            >>> font.kerning.items()
            [-20, -15, 5]
        """
        return super(BaseKerning, self).values()
