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
        (Are contours, components, and anchors needed for countour?)
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
