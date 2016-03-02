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
