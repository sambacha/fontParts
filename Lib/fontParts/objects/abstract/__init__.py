"""
The goal is to define a very clean scripting API
that preserves the main functionality of RoboFab.
Say something about the importance of script
portability. Designers have workflows and specific
binary requirements, etc.

Things that should be considered for removal:
- anything that does anything too magical.
- anything that was originally implemented for
  environment specific reasons.
- anything that was designed as a speed optimization.

Things that haven't been defined, but should.
- a common error instead of relying on the environment
  errors. those often differ from environment
  to environment and that's a portability problem.
- what errors should be raised by each method

Things that we should consider adding:
- a naming convention for environment specific
  things. for example, it would be bad if two
  environments defined "makeMyFont" but they took
  different arguments and did different things.
- a parent tree system like in defcon. this would
  replace the fragile getParent.
"""

class BaseObject(object):
    """
    A base object for everything.
    I'm not sure how this will work with subclassing.
    """

    def update(self):
        """
        Tell the environment that something has changed in
        the object. The behavior of this method will vary
        from environment to environment.
        """

    def naked(self):
        """
        Return the wrapped object itself, in case it is needed for direct access.
        """

    def getParent(self):
        """
        - this is not sufficient anymore
        """

    # ----
    # Math
    # ----

    def __mul__(self, factor):
        pass

    __rmul__ = __mul__

    def __div__(self, factor):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


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


class BaseGlyph(BaseObject):

    # ----------
    # Attributes
    # ----------

    """
    - lib
    - contours
    - components
    - anchors
    - width
    - note
    - unicodes
    - unicode
    - selected (how do we define what this means?)
    - psHints (this should be removed)
    - box: The bounding box of the glyph: (xMin, yMin, xMax, yMax).
        - rename this to bounds?
        - The object returned should let None be the same as (0, 0, 0, 0)
          because lots of things want to know None but for backwards compatibility
          we can't switch to returning None.
          (Currently if there are no outlines, None is returned)
    - leftmargin: The left margin.
    - rightMargin: The right margin.
    - angledLeftMargin (add this?)
    - angledRightMargin (add this?)
    - mark (this will need to be backwards compatible)
    """

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    # ----------
    # Glyph Math
    # ----------

    def __mul__(self, factor):
        pass

    __rmul__ = __mul__

    def __div__(self, factor):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    # ----
    # Pens
    # ----

    def getPen(self):
        """
        Return a Pen object for creating an outline in this glyph.
        """

    def getPointPen(self):
        """
        Return a PointPen object for creating an outline in this glyph.
        """

    def draw(self, pen):
        """
        Draw the object with a RoboFab segment pen.

        - add some kwargs about what data should be drawn?
        """

    def drawPoints(self, pen):
        """
        Draw the object with a point pen.
        
        - add some kwargs about what data should be drawn?
        """

    # --------
    # Contours
    # --------

    def appendContour(aContour, offset=(0, 0)):
        """
        Append a contour to the glyph.

        - note that it is copied, not inserted as is.
        """

    def removeContour(index):
        """
        Remove a specific contour from the glyph.
        """

    def clearContours():
        """
        Clear all contours.
        """

    def removeOverlap(self):
        """Remove overlap"""

    # ----------
    # Components
    # ----------

    def appendComponent(baseGlyph, offset=(0, 0), scale=(1, 1)):
        """
        Append a component to the glyph.
        """

    def removeComponent(component):
        """
        Remove  a specific component from the glyph.
        """

    def clearComponents():
        """
        Clear all components.
        """

    def decompose():
        """
        Decompose all components.
        """

    def getComponents():
        """
        Returns a list with all components in the glyph.

        - what is this for?
        """

    # -------
    # Anchors
    # -------

    def appendAnchor(name, position, mark=None):
        """
        Append an anchor to the glyph.

        - mark may be limiting
        """

    def removeAnchor(anchor):
        """
        Remove  a specific anchor from the glyph.
        """

    def clearAnchors():
        """
        Clear all anchors.
        """

    def getAnchors():
        """
        Returns a list with all anchors in the glyph.

        - what is this for?
        """

    # ------------------
    # Data Normalization
    # ------------------

    def round(self):
        """
        Round all coordinates in all contours, components and anchors.
        """

    def correctDirection(self, trueType=False):
        """
        Correct the direction of the contours in the glyph.
        """

    def autoContourOrder(self):
        """
        Attempt to sort the contours based on their centers.

        - centers isn't the best way to do this.
        """

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this glyph. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y), contours=True, components=True, anchors=True):
        """
        Move a glyph’s items that are flagged as ``True``.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the glyph.
        """

    def rotate(angle, offset=None):
        """
        Rotate the glyph.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the glyph.

        - the center should be definable.
        """

    def center(padding=None):
        """
        Equalise sidebearings, set to padding if wanted.

        - this should be removed
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minGlyph, maxGlyph, suppressError=True, analyzeOnly=False):
        """
        Traditional interpolation method. Interpolates by factor between
        minGlyph and maxGlyph.

        Args:
            - suppressError: will supress all tracebacks
            - analyzeOnly: will not perform the interpolation, but analyze all glyphs
              and return a dict of problems
        """

    def isCompatible(self, otherGlyph, report=True):
        """
        Return a bool value if the glyph is compatible with otherGlyph.
        With report = True, isCompatible will return a report of what’s wrong.
        The interpolate method requires absolute equality between contour data.
        Absolute equality is preferred among component and anchor data, but it
        is NOT required. Interpolation between components and anchors will only
        deal with compatible data and incompatible data will be ignored. This
        method reflects this system.

        - this needs to be thought through
        """

    # ------------
    # Data Queries
    # ------------

    def pointInside((x, y), evenOdd=0):
        """
        Determine if the point is in the black or white of the glyph.
        """

    def rasterize(cellSize=50, xMin=None, yMin=None, xMax=None, yMax=None):
        """
        Slice the glyph into a grid based on the cell size. 

        Returns:
            A list of lists containing bool values that indicate the
            black (True) or white (False) value of that particular cell.
            These lists are arranged from top to bottom of the glyph and
            proceed from left to right.

        - this should be removed
        """

    # ----
    # Misc
    # ----

    def autoUnicodes(self):
        """
        see BaseFont.autoUnicodes
        """

    def appendGlyph(aGlyph, offset=(0, 0)):
        """
        Append another glyph to the glyph.

        - note that the data is copied, not inserted.
        """

    def copy(self, aParent=None):
        """
        Copy this glyph.

        - need to define where the copy goes.
        - what is aParent?
        """

    def clear(contours=True, components=True, anchors=True, guides=True):
        """
        Clear all items marked as True from the glyph.
        """

    def getGlyph(self, name):
        """
        Provided there is a font parent for this glyph, return a sibling glyph.

        - this should be removed
        """

    def isEmpty(self):
        """
        Return true if the glyph has no contours or components

        - this should be removed.
        """

    def deSelect(self):
        """
        Set all selected attrs in glyph to False: for the glyph, components, anchors, points.

        - this is important, but is this the best API?
        """


class BaseContour(BaseObject):

    # ----------
    # Attributes
    # ----------
    """
    - box (see glyph.box)
    - clockwise
    - segments
    - index
    - points
    - bPoints
    - selected
    """

    def __repr__(self):
        pass

    def __len__(self):
        pass

    # ----
    # Pens
    # ----

    def draw(self, pen):
        pass

    def drawPoints(self, pen):
        pass

    # ------------------
    # Data normalization
    # ------------------

    def autoStartSegment(self):
        """
        automatically set the lower left point of
        the contour as the first point.
        """

    def round(self):
        """
        round the value of all points in the contour
        """

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this contour. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y), contours=True, components=True, anchors=True):
        """
        Move a glyph’s items that are flagged as ``True``.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the contour.
        """

    def rotate(angle, offset=None):
        """
        Rotate the contour.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the contour.

        - the center should be definable.
        """

    def reverseContour(self):
        """
        reverse the contour
        """

    # ------------
    # Data Queries
    # ------------

    def pointInside(self, (x, y), evenOdd=0):
        """
        determine if the point is inside or ouside of the contour
        """

    # ----
    # Misc
    # ----

    def copy(self, aParent=None):
        """
        Duplicate this contour

        - what is aParent?
        """

    # --------
    # Segments
    # --------

    def appendSegment(self, segmentType, points, smooth=False):
        """
        append a segment to the contour
        """

    def insertSegment(self, index, segmentType, points, smooth=False):
        """
        insert a segment into the contour
        """

    def removeSegment(self, index):
        """
        remove a segment from the contour
        """

    def setStartSegment(self, segmentIndex):
        """
        set the first segment on the contour
        """

    # -------
    # bPoints
    # -------

    def appendBPoint(self, pointType, anchor, bcpIn=(0, 0), bcpOut=(0, 0)):
        """
        append a bPoint to the contour
        """

    def insertBPoint(self, index, pointType, anchor, bcpIn=(0, 0), bcpOut=(0, 0)):
        """
        insert a bPoint at index on the contour
        """


class BaseSegment(BaseObject):

    # ----------
    # Attributes
    # ----------
    """
    - onCurve
    - offCurve
    - smooth
    - points
    - type
    - index
    - selected
    """

    def __repr__(self):
        pass

    def __len__(self):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this segment. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y)):
        """
        Move the segment.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the segment.
        """

    def rotate(angle, offset=None):
        """
        Rotate the segment.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the segment.

        - the center should be definable.
        """

    # ------
    # Points
    # ------

    def insertPoint(self, index, pointType, point):
        pass

    def removePoint(self, index):
        pass

    # ----
    # Misc
    # ----

    def copy(self, aParent=None):
        """
        Duplicate this segment

        - what is aParent?
        """


class BasePoint(BaseObject):

    # ----------
    # Attributes
    # ----------
    """
    - selected
    - x
    - y
    - type
    - name
    - index
    """

    def __repr__(self):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this point. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y)):
        """
        Move the point.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the point.
        """

    def rotate(angle, offset=None):
        """
        Rotate the point.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the point.

        - the center should be definable.
        """

    # ----
    # Misc
    # ----

    def round(self):
        pass

    def copy(self, aParent=None):
        """
        Duplicate this point
        """


class BaseBPoint(BaseObject):


    # ----------
    # Attributes
    # ----------
    """
    - selected
    - index
    - anchor
    - bcpIn
    - bcpOut
    - type
    """

    def __repr__(self):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this point. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y)):
        """
        Move the point.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the point.
        """

    def rotate(angle, offset=None):
        """
        Rotate the point.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the point.

        - the center should be definable.
        """

    # ----
    # Misc
    # ----

    def round(self):
        pass

    def copy(self, aParent=None):
        """
        Duplicate this point
        """


class BaseComponent(BaseObject):

    # ----------
    # Attributes
    # ----------
    """
    - selected
    - index
    - baseGlyph
    - offset
    - scale
    - transformation
    """

    def __repr__(self):
        pass

    # ----
    # Pens
    # ----

    def draw(self, pen):
        pass

    def drawPoints(self, pen):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this component. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y)):
        """
        Move the component.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the component.
        """

    def rotate(angle, offset=None):
        """
        Rotate the component.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the component.

        - the center should be definable.
        """

    # ----
    # Misc
    # ----

    def decompose(self):
        pass

    def round(self):
        pass

    def copy(self, aParent=None):
        """
        Duplicate this component
        """


class BaseAnchor(BaseObject):

    # ----------
    # Attributes
    # ----------
    """
    - selected
    - index
    - x
    - y
    - position (is this needed?)
    - mark
    """

    def __repr__(self):
        pass

    # ----
    # Pens
    # ----

    def draw(self, pen):
        pass

    def drawPoints(self, pen):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this anchor. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y)):
        """
        Move the anchor.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the anchor.
        """

    def rotate(angle, offset=None):
        """
        Rotate the anchor.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the anchor.

        - the center should be definable.
        """

    # ----
    # Misc
    # ----

    def round(self):
        pass

    def copy(self, aParent=None):
        """
        Duplicate this anchor
        """


class BaseInfo(BaseObject):
    pass

class BaseKerning(BaseObject):
    pass

class BaseGroups(BaseObject):
    pass

class BaseLib(BaseObject):
    pass