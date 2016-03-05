from base import BaseObject, dynamicProperty

class BaseLayer(BaseObject):

    """
    XXX

    Add some tips on how to make this object when the
    editor has a glyph level layer model instead of
    a font level layer model.

    XXX
    """

    # --------------
    # Identification
    # --------------

    name = dynamicProperty("name", "The name of the layer.")

    def _get_name(self):
        self.raiseNotImplementedError()

    def _set_name(self):
        self.raiseNotImplementedError()

    color = dynamicProperty("color", "The layer's color. XXX need to determine the data type")

    def _get_color(self):
        self.raiseNotImplementedError()

    def _set_color(self):
        self.raiseNotImplementedError()

    # -----------
    # Sub-Objects
    # -----------

    # lib

    lib = dynamicProperty("lib", "The font's lib object.")

    def _get_lib(self):
        self.raiseNotImplementedError()

    # -----------------
    # Glyph Interaction
    # -----------------

    def __len__(self):
        """
        The number of glyphs in the layer.
        """

    def __iter__(self):
        """
        Iterate through the glyphs in the layer.
        """

    def __getitem__(self, name):
        """
        Get the glyph with name from the  layer.
        """

    def keys(self):
        """
        Get a list of all glyphs in the layer of the font.
        The order of the glyphs is undefined.
        """

    def __contains__(self, name):
        """
        Test if the layer contains a glyph with name.
        """

    has_key = __contains__

    def newGlyph(self, name, clear=True):
        """
        Make a new glyph in the layer. The glyph will
        be returned.

        clear indicates if the data in an existing glyph
        with the same name should be cleared. If so,
        the clear method of the glyph should be called.
        """

    def removeGlyph(self, name):
        """
        Remove the glyph with name from the layer.
        """

    def insertGlyph(self, glyph, name=None):
        """
        Insert a new glyph into the layer. The glyph will
        be returned.

        name indicates the name that should be assigned to
        the glyph after insertion. If name is not given,
        the glyph's original name must be used. If the glyph
        does not have a name, an error must be raised.

        This does not insert the given glyph object. Instead,
        a new glyph is created and the data from the given
        glyph is recreated in the new glyph.
        """

    # -----------------
    # Global Operations
    # -----------------

    def round(self):
        """
        Round all approriate data to integers. This is the
        equivalent of calling the round method on each object
        within the layer.
        """

    def autoUnicodes(self):
        """
        Use heuristics to determine Unicode values to all glyphs
        and set the values in the glyphs. Environments will define
        their own heuristics for automatically determining values.
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minLayer, maxLayer, suppressError=True, analyzeOnly=False, showProgress=False):
        """
        Interpolate all possible data in the layer. The interpolation
        occurs on a 0 to 1.0 range where minLayer is located at
        0 and maxLayer is located at 1.0.

        factor is the interpolation value. It may be less than 0
        and greater than 1.0. It may be a number (integer, float)
        or a tuple of two numbers. If it is a tuple, the first
        number indicates the x factor and the second number
        indicates the y factor.

        suppressError indicates if incompatible data should be ignored
        or if an error should be raised when such incompatibilities are found.

        analyzeOnly indicates if the intrpolation should only be a
        compatibiltiy check with no interpolation actually performed.
        If this is True, a dict of compatibility problems will
        be returned.
        """

    # ------------------
    # Reference Mappings
    # ------------------

    def getCharacterMapping(self):
        """
        Get a dictionary showing unicode to glyph mapping.

            {
                unicode value : [glyph names]
            }
        """

    def getReverseComponentMapping(self):
        """
        Get a dictionary showing component references.

            {
                base glyph name : [glyph names]
            }
        """