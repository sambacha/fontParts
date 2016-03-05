from base import BaseObject, dynamicProperty

class BaseFont(BaseObject):

    def __repr__(self):
        pass

    def __eq__(self):
        """
        XXX

        How should this be implemented?
        Path comparison? Data comparison?
        Maybe we should just remove it.

        XXX
        """

    # ---------------
    # File Operations
    # ---------------

    path = dynamicProperty("path", "The path to the file this object represents.")

    def _get_path(self):
        self.raiseNotImplementedError()

    def open(self, path, showInterface=True):
        """
        Open the file located at path. The type of files
        that can be opened will be defined by the environment.

        showInterface indicates if the user interface
        should be opened or not. Environments may or may not
        implement this behavior.
        """
        self.raiseNotImplementedError()

    def save(self, path=None, showProgress=False, formatVersion=None):
        """
        Save the font to path. If path is None, use the font's
        original location. The file type must be inferred from
        the file extension on the given path. If no file extension
        is given, the environment may fall back to the format
        of its choice.

        showProgress indicates if a progress indicator should be
        displayed during the operation. Environments may or may not
        implement this behavior.

        formatVersion indicates the format version that should
        be used for writing the given file type. For example, if
        2 is given for formatVersion and the file type being written
        if UFO, the file is to be written in UFO 2 format. This
        value is not limited to UFO format versions. If no
        format version is given, the original format version of
        the file should be preserved. If there is no original
        format version it is implied that the format version
        is the latest version for the file type as supported
        by the environment.

        Environments may define their own rules governing when
        a file should be saved into its original location and
        when it should not. For example, a font opened from a
        compiled OpenType font may not be written back into
        the original OpenType font.
        """
        self.raiseNotImplementedError()

    def close(self, save=False):
        """
        Close the font. If save is True, call the save method
        is called with no arguments.
        """
        self.raiseNotImplementedError()

    def generate(self, format, path=None):
        """
        Generate the font to another format.

        format defines the file format to output. These are the standard

        mactype1     = Mac Type 1 font (generates suitcase  and LWFN file)
        macttf       = Mac TrueType font (generates suitcase)
        macttdfont   = Mac TrueType font (generates suitcase with resources in data fork)
        otfcff       = PS OpenType (CFF-based) font (OTF)
        otfttf       = PC TrueType/TT OpenType font (TTF)
        pctype1      = PC Type 1 font (binary/PFB)
        pcmm         = PC MultipleMaster font (PFB)
        pctype1ascii = PC Type 1 font (ASCII/PFA)
        pcmmascii    = PC MultipleMaster font (ASCII/PFA)
        ufo1         = UFO format version 1
        ufo2         = UFO format version 2
        ufo3         = UFO format version 3
        unixascii    = UNIX ASCII font (ASCII/PFA)

        Environments are not required to support all of these.
        Environments may define their own format types.

        path defines the location where the new file should
        be located. If path defines a directory, the file should
        be output as the current file name, with the appropriate
        suffix for the format, into the given directory. If no path
        is given, the file will be output into the same directory
        as the source font with the file named with the current
        file name, with the appropriate suffix for the format.
        """
        self.raiseNotImplementedError()

    # -----------
    # Sub-Objects
    # -----------

    # info

    info = dynamicProperty("info", "The font's info object.")

    def _get_info(self):
        self.raiseNotImplementedError()

    # groups

    groups = dynamicProperty("groups", "The font's groups object.")

    def _get_groups(self):
        self.raiseNotImplementedError()

    # kerning

    kerning = dynamicProperty("kerning", "The font's kerning object.")

    def _get_kerning(self):
        self.raiseNotImplementedError()

    # features

    features = dynamicProperty("features", "The font's features object.")

    def _get_features(self):
        self.raiseNotImplementedError()

    # lib

    lib = dynamicProperty("lib", "The font's lib object.")

    def _get_lib(self):
        self.raiseNotImplementedError()

    # layers

    layers = dynamicProperty("layers", "The font's layers.")

    def _get_layers(self):
        self.raiseNotImplementedError()

    # -----------------
    # Layer Interaction
    # -----------------

    """
    XXX

    Need to carefully document the naming
    regarding the default layer. the user
    shouldn't be presented with the UFO
    defined default name. that should be
    indicated with None.

    XXX
    """

    layers = dynamicProperty("layers", "The font's layer objects.")

    def _get_layers(self):
        """
        XXX

        this needs to return a special immutable list
        only len, __iter__ and __getitem__ should work.
        we don't want that list being manipulated.
        manipulation should happen in the font.

        XXX
        """
        self.raiseNotImplementedError()

    layerOrder = dynamicProperty("layerOrder", "A list of layer names indicating order of the layers in the font.")

    def _get_layerOrder(self):
        self.raiseNotImplementedError()

    def _set_layerOrder(self, value):
        self.raiseNotImplementedError()

    defaultLayer = dynamicProperty("defaultLayer", "The name of the font's default layer.")

    def _get_defaultLayer(self):
        self.raiseNotImplementedError()

    def _set_defaultLayer(self, value):
        self.raiseNotImplementedError()

    def getLayer(self, name):
        """
        Get the layer with name.
        """

    def newLayer(self, name, color=None):
        """
        Make a new layer with name and color.
        """
        self.raiseNotImplementedError()

    def removeLayer(self, layer):
        """
        Remove the layer from the font.
        """
        self.raiseNotImplementedError()

    # -----------------
    # Glyph Interaction
    # -----------------

    def __len__(self):
        """
        The number of glyphs in the default layer.
        """

    def __iter__(self):
        """
        Iterate through the glyphs in the default layer.
        """

    def __getitem__(self, name):
        """
        Get the glyph with name from the default layer.
        """

    def keys(self):
        """
        Get a list of all glyphs in the default layer
        of the font. The order of the glyphs is undefined.
        """

    def __contains__(self, name):
        """
        Test if the default layer contains a glyph with name.
        """

    has_key = __contains__

    def newGlyph(self, name, clear=True):
        """
        Make a new glyph in the default layer. The
        glyph will be returned.

        clear indicates if the data in an existing glyph
        with the same name should be cleared. If so,
        the clear method of the glyph should be called.
        """

    def removeGlyph(self, name):
        """
        Remove the glyph with name from the default layer.
        """

    def insertGlyph(self, glyph, name=None):
        """
        Insert a new glyph into the default layer.
        The glyph will be returned.

        name indicates the name that should be assigned to
        the glyph after insertion. If name is not given,
        the glyph's original name must be used. If the glyph
        does not have a name, an error must be raised.

        This does not insert the given glyph object. Instead,
        a new glyph is created and the data from the given
        glyph is recreated in the new glyph.
        """

    glyphOrder = dynamicProperty("glyphOrder", "The preferred order of the glyphs in the font.")

    def _get_glyphOrder(self):
        self.raiseNotImplementedError()

    def _set_glyphOrder(self, value):
        self.raiseNotImplementedError()

    # -----------------
    # Global Operations
    # -----------------

    def round(self):
        """
        Round all approriate data to integers. This is the
        equivalent of calling the round method on each object
        within the font.

        This applies only to the default layer.
        """

    def autoUnicodes(self):
        """
        Use heuristics to determine Unicode values to all glyphs
        and set the values in the glyphs. Environments will define
        their own heuristics for automatically determining values.

        This applies only to the default layer.
        """

    # ----------
    # Guidelines
    # ----------

    guidelines = dynamicProperty("guidelines", "An ordered list of font level guidelines.")

    def _get_guidelines(self):
        self.raiseNotImplementedError()

    def appendGuideline(self, position, angle, name=None, color=None):
        """
        Append a new guideline to the font.

        position (x, y) indicates the position of the guideline.

        angle indicates the angle of the guideline.

        name indicates the name for the guideline.

        color indicates the color for the guideline.
        """
        self.raiseNotImplementedError()

    def removeGuideline(self, guideline):
        """
        Remove guideline from the font.
        """
        self.raiseNotImplementedError()

    def clearGuidelines(self):
        """
        Clear all font level guidelines.
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minFont, maxFont, suppressError=True, analyzeOnly=False, showProgress=False):
        """
        Interpolate all possible data in the font. The interpolation
        occurs on a 0 to 1.0 range where minFont is located at
        0 and maxFont is located at 1.0.

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

        This applies only to the default layer.
        """

    def getReverseComponentMapping(self):
        """
        Get a dictionary showing component references.

            {
                base glyph name : [glyph names]
            }

        This applies only to the default layer.
        """