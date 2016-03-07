from base import BaseObject, dynamicProperty

class BaseGlyph(BaseObject):

    """
    XXX

    - angledLeftMargin (add this?)
    - angledRightMargin (add this?)

    XXX
    """

    def copy(self):
        """
        Copy this glyph by duplicating the data into
        a glyph that does not belong to a font.
        """

    # --------------
    # Identification
    # --------------

    # Name

    name = dynamicProperty("name", "The glyph's name.")

    def _get_name(self):
        self.raiseNotImplementedError()

    def _set_name(self, value):
        self.raiseNotImplementedError()

    # Unicodes

    unicodes = dynamicProperty("unicodes", "The glyph's unicode values in order from most to least important.")

    def _get_unicodes(self):
        self.raiseNotImplementedError()

    def _set_unicodes(self, value):
        self.raiseNotImplementedError()

    unicode = dynamicProperty("unicode", "The glyph's primary unicode value.")

    def _get_unicode(self):
        pass

    def _set_unicode(self, value):
        pass

    def autoUnicodes(self):
        """
        Use heuristics to determine the Unicode values for the glyph.
        Environments will define their own heuristics for automatically
        determining values.
        """
        self.raiseNotImplementedError()

    # -------
    # Metrics
    # -------

    width = dynamicProperty("width", "The glyph's width.")

    def _get_width(self):
        self.raiseNotImplementedError()

    def _set_width(self, value):
        self.raiseNotImplementedError()

    leftMargin = dynamicProperty("leftMargin", "The glyph's left margin.")

    def _get_leftMargin(self):
        pass

    def _set_leftMargin(self, value):
        pass

    rightMargin = dynamicProperty("rightMargin", "The glyph's right margin.")

    def _get_rightMargin(self):
        pass

    def _set_rightMargin(self, value):
        pass

    height = dynamicProperty("height", "The glyph's height.")

    def _get_height(self):
        self.raiseNotImplementedError()

    def _set_height(self, value):
        self.raiseNotImplementedError()

    # ----
    # Math
    # ----

    """
    The basics of font math need to be defined somewhere.
    """

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
        Return a Pen object for modifying the glyph.
        """
        self.raiseNotImplementedError()

    def getPointPen(self):
        """
        Return a PointPen object for modifying the glyph.
        """
        self.raiseNotImplementedError()

    def draw(self, pen):
        """
        Draw the glyph with the given Pen.

        XXX: add some kwargs about what data should be drawn?
        """

    def drawPoints(self, pen):
        """
        Draw the glyph with the given PointPen.
        
        XXX: add some kwargs about what data should be drawn?
        """

    # -----------------------------------------
    # Contour, Component and Anchor Interaction
    # -----------------------------------------

    def clear(self):
        """
        Clear all contours, components and anchors from the glyph.
        """

    # Contours

    contours = dynamicProperty("contours")

    def _get_contours(self):
        pass

    def __getitem__(self, index):
        pass

    def __iter__(self):
        pass

    def appendContour(self, contour, offset=None):
        """
        A copy of the given contour to the glyph.

        offset indicates the distance that the
        contour should be offset when added to
        the glyph. The default is (0, 0).
        """

    def removeContour(self, index):
        """
        Remove the contour with index from the glyph.
        """
        self.raiseNotImplementedError()

    def clearContours():
        """
        Clear all contours.
        """
        self.raiseNotImplementedError()

    def removeOverlap(self):
        """
        Perform a remove overlap operation on the contours.
        """
        self.raiseNotImplementedError()

    # Components

    components = dynamicProperty("components")

    def _get_components(self):
        self.raiseNotImplementedError()

    def appendComponent(self, baseGlyph, offset=None, scale=None):
        """
        Append a new component to the glyph.

        baseGlyph indicates the glyph that the
        component will reference.

        offset indictaes the offset that should
        be defined in the component. The default
        is (0, 0).

        scale indicates the scale that should be
        defined in the component. The default is
        (1.0, 1.0).
        """

    def removeComponent(self, component):
        """
        Remove component from the glyph.
        """
        self.raiseNotImplementedError()

    def clearComponents(self):
        """
        Clear all components.
        """
        self.raiseNotImplementedError()

    def decompose(self):
        """
        Decompose all components.
        """

    # Anchors

    anchors = dynamicProperty("anchors")

    def _get_anchors(self):
        self.raiseNotImplementedError()

    def appendAnchor(self, name, position, mark=None):
        """
        Append a new anchor to the glyph.

        name indicates the name that should be
        assigned to the anchor.

        position is an (x, y) tuple defining
        the position for the anchor.

        XXX define mark
        """

    def removeAnchor(self, anchor):
        """
        Remove anchor from the glyph.
        """
        self.raiseNotImplementedError()

    def clearAnchors():
        """
        Clear all anchors.
        """
        self.raiseNotImplementedError()

    def appendGlyph(self, other, offset=None):
        """
        Append copies of the contours, components
        and anchors from other.

        offset indicates the offset that should
        be applied to the appended data. The default
        is (0, 0).
        """

    # ----------
    # Guidelines
    # ----------

    guidelines = dynamicProperty("guidelines", "An ordered list of glyph level guidelines.")

    def _get_guidelines(self):
        self.raiseNotImplementedError()

    def appendGuideline(self, position, angle, name=None, color=None):
        """
        Append a new guideline to the glyph.

        position (x, y) indicates the position of the guideline.

        angle indicates the angle of the guideline.

        name indicates the name for the guideline.

        color indicates the color for the guideline.
        """
        self.raiseNotImplementedError()

    def removeGuideline(self, guideline):
        """
        Remove guideline from the glyph.
        """
        self.raiseNotImplementedError()

    def clearGuidelines(self):
        """
        Clear all guidelines in the glyph.
        """

    # ------------------
    # Data Normalization
    # ------------------

    def round(self):
        """
        Round coordinates in all contours, components and anchors.
        """

    def correctDirection(self, trueType=False):
        """
        Correct the direction of the contours in the glyph.
        """

    def autoContourOrder(self):
        """
        Sort the contours based on their centers.
        """

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the glyph with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the contours, components and anchors
        in the glyph by value. Value must be a tuple
        defining x and y values.
        """

    def scale((x, y), center=None):
        """
        Scale the contours, components and anchors
        in the glyph by value. Value must be a tuple
        defining x and y values.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the contours, components and anchors
        in the glyph by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the contours, components and anchors
        in the glyph by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minGlyph, maxGlyph, suppressError=True, analyzeOnly=False):
        """
        Interpolate all possible data in the glyph. The interpolation
        occurs on a 0 to 1.0 range where minGlyph is located at
        0 and maxGlyph is located at 1.0.

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

    def isCompatible(self, otherGlyph, report=True):
        """
        Returns a boolean indicating if the glyph is compatible for
        interpolation with otherGlyph. If report is True, a list
        of errors will be returned with the boolean.
        """

    # ------------
    # Data Queries
    # ------------

    def pointInside(self, point, evenOdd=False):
        """
        Determine if point is in the black or white of the glyph.

        point must be an (x, y) tuple.
        XXX define evenOdd
        """

    box = dynamicProperty("box", "The bounding box of the glyph: (xMin, yMin, xMax, yMax) or None.")

    def _get_box(self):
        """
        XXX

        The object returned should let None be the same as (0, 0, 0, 0)
        because lots of things want to know None but for backwards compatibility
        we can't switch to returning None.
        (Currently if there are no outlines, None is returned in some environments and (0, 0, 0, 0) in others)

        XXX
        """

    # -----------------
    # Layer Interaction
    # -----------------

    layers = dynamicProperty("layers", "The glyph's layers. Each layer will be a glyph object.")

    def _get_layers(self):
        """
        XXX

        this needs to return a special immutable list
        only len, __iter__ and __getitem__ should work.
        we don't want that list being manipulated.
        manipulation should happen in the font/glyph.

        XXX
        """
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
        Remove the layer from the glyph (not the font).
        """
        self.raiseNotImplementedError()

    # ----
    # Misc
    # ----

    markColor = dynamicProperty("markColor", "The mark color for the glyph.")

    def _get_markColor(self):
        self.raiseNotImplementedError()

    def _set_markColor(self, value):
        """
        Accept a two value formats:

        - standard color tuple
        - integer: 0-255
            0 means no color. When the value is greater than 0,
            the color is the hue value in a HSV color system.
            The full HSV value will be (hue, 255, 255). If the
            hue value is > 255, make it 255. This HSV value
            is then converted to an RGB value using the standard
            algorithm. The new color tuple is then (r, g, b, 0.5).

        import colorsys
        r, g, b = colorsys.hsv_to_rgb(i, 1.0, 1.0)
        a = 0.5
        color = (r, g, b, a)
        """
        self.raiseNotImplementedError()

    # Note

    note = dynamicProperty("note", "A note for the glyph.")

    def _get_note(self):
        self.raiseNotImplementedError()

    def _set_note(self, value):
        self.raiseNotImplementedError()

    # Lib

    lib = dynamicProperty("lib", "The lib for the glyph.")

    def _get_lib(self):
        self.raiseNotImplementedError()

    # Image

    image = dynamicProperty("image", "The image for the glyph.")

    def _get_image(self):
        self.raiseNotImplementedError()

    def _set_image(self, value):
        self.raiseNotImplementedError()
