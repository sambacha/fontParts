class BaseGroups(BaseObject):

    # needs all dict methods that make sense

    def __repr__(self):
        pass

    def __getitem__(self, name):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key, value):
        pass

    def findGlyph(self, glyphName):
        """
        return a list of all groups contianing glyphName
        """
