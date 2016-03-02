class BaseFont(BaseObject):

    # ----------
    # Attributes
    # ----------

    """
    - path
    - info
    - kerning
    - groups
    - features
    - lib
    - psHints (this should be removed)
    """

    def __repr__(self):
        pass

    def __eq__(self):
        """
        - this has historically been tricky
        """
        pass

    def __len__(self):
        pass

    # ---------------
    # File Operations
    # ---------------

    def open(self, path):
        """
        Open the file located at path.

        The type of files that can be opened will be defined
        by the environment.
        """

    def save(self, path=None, doProgress=False, formatVersion=2):
        """
        Save the font to the file located at path.
        If path is None, use the font's original location.

        - rename doProgress to showProgress
        - formatVersion is UFO specific, but maybe it's okay.
          the default could be None which would indicate that
          the format version should be preserved if the file
          exists or the format version should be the latest
          UFO version supported by the environment. the format
          version also don't have to be UFO specific. It could
          indicate a non-UFO format version. For example, when
          saving in FontLab "1" could mean VFB.
        - some rules need to be established about saving to
          the original location. for example, if the font
          started as a binary, does it go back into that binary?
          (obviously not.)
        """

    def close(self, save=False):
        """
        Close the font. If save is True, call the save method
        with no values given for the possible arguments..
        """

def generate(self, outputType, path=None):
        """
        generate the font. outputType is the type of font to ouput.
        --Ouput Types:
        'pctype1'   :   PC Type 1 font (binary/PFB)
        'pcmm'      :   PC MultipleMaster font (PFB)
        'pctype1ascii'  :   PC Type 1 font (ASCII/PFA)
        'pcmmascii' :   PC MultipleMaster font (ASCII/PFA)
        'unixascii' :   UNIX ASCII font (ASCII/PFA)
        'mactype1'  :   Mac Type 1 font (generates suitcase  and LWFN file)
        'otfcff'        :   PS OpenType (CFF-based) font (OTF)
        'otfttf'        :   PC TrueType/TT OpenType font (TTF)
        'macttf'    :   Mac TrueType font (generates suitcase)
        'macttdfont'    :   Mac TrueType font (generates suitcase with resources in data fork)
                    (doc adapted from http://dev.fontlab.net/flpydoc/)
        
        path can be a directory or a directory file name combo:
        path="DirectoryA/DirectoryB"
        path="DirectoryA/DirectoryB/MyFontName"
        if no path is given, the file will be output in the same directory
        as the vfb file. if no file name is given, the filename will be the
        vfb file name with the appropriate suffix.

        - this is a mess and different environments support different things.
        """

    # -----------------------
    # Global Glyph Operations
    # -----------------------

    def round(self):
        """
        Round all of the points in all of the glyphs.

        - should this have a value option?
        - at this level, it seems like this should
          round everything (kerning, info, etc.)
          not just point coordinates.
        """

    def autoUnicodes(self):
        """
        Using fontTools.agl, assign Unicode lists to all glyphs in the font.

        - the dependence on AGL should probably be
          droppen in favor of a statement that the
          technique used will be environment specific.
        """

    # ------------------
    # Reference Mappings
    # ------------------

    def getCharacterMapping(self):
        """
        Create a dictionary of unicode -> [glyphname, ...] mappings.
        """

    def getReverseComponentMapping(self):
        """
        Get a reversed map of component references in the font.
        """

    # -----------------
    # Glyph Interaction
    # -----------------

    def __iter__(self):
        pass

    def __getitem__(self, name):
        """
        Get the glyph with name.
        """

    def keys(self):
        """
        Get a list of all glyphs in the font.

        - should this use any defined glyph order?
        """

    def __contains__(self, name):
        """
        Test if font contains a glyph with name.
        """

    def has_key(self, name):
        """
        Same as __contains__.

        - get rid of this? maybe not since
          it's harmless and lots of people
          probably use it. does Python 3's
          dict have has_key?
        """

    def getGlyph(self, name):
        """
        Return a glyph with name.

        - I think this was an internal function
          that loaded a glyph it needed to be loaded
          or pulled it from a cache. we should probably
          remove this from the API.
        """

    def getWidth(self, name):
        """
        What is this? We should get rid of it.
        """

    def newGlyph(self, name, clear=True):
        """
        Make a new glyph with ``glyphName``.

        Args:
        clear: If the glyph exists and clear=True, clear the glyph.
        """

    def removeGlyph(self, name):
        """
        Remove the glyph with name from the font.
        """

    def insertGlyph(self, glyph, name=None):
        """
        Insert a new glyph into the font.

        Returns:
        The new glyph which has been inserted.

        - define the name behavior
        - explain that this makes a copy of the glyph
          rather than inserting the provided object.
        """

    def compileGlyph(glyphName, baseName, accentNames, adjustWidth=False, preflight=False, printErrors=True):
        """
        Compile components into a new glyph using components and anchorpoints.

        Args:
            - glyphName: the name of the glyph where it all needs to go
            - baseName: the name of the base glyph
            - accentNames: a list of accentName, anchorName tuples, [(‘acute’, ‘top’), etc]

        - I think this should be removed. It has been eclipsed
          by far superior environment specific glyph compilers.
        """

    def generateGlyph(glyphName, replace=1, preflight=False, printErrors=True):
        """
        Generate a glyph and return it. Assembled from GlyphConstruction.txt

        - This should be removed.
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(factor, minFont, maxFont, suppressError=True, analyzeOnly=False, doProgress=False):
        """
        Traditional interpolation method. Interpolates by factor between minFont and maxFont.

        Args:
            - suppressError: will supress all tracebacks
            - analyzeOnly: will not perform the interpolation, but analyze all glyphs and return a dict of problems
        """