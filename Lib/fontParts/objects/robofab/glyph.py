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