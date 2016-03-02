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