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