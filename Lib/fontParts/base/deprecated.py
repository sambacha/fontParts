"""
A collection of deprecated roboFab methods.
Those methods are added to keep scripts and code compatible.
"""


# ========
# = base =
# ========

class DeprecatedBase(object):

    def setParent(self, parent):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.setParent()'" % objName

    def update(self):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.update': use %s.changed()" % (objName, objName)
        self.changed()

    def setChanged(self):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.setChanged': use %s.changed()" % (objName, objName)
        self.changed()


# ==================
# = transformation =
# ==================

class DeprecatedTransformation(object):

    def move(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.move()': use %s.moveBy()" % (objName, objName)
        self.moveBy(*args, **kwargs)

    def translate(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.translate()': use %s.moveBy()" % (objName, objName)
        self.moveBy(*args, **kwargs)

    def scale(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.scale()': use %s.scaleBy()" % (objName, objName)
        self.scaleBy(*args, **kwargs)

    def rotate(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.rotate()': use %s.rotateBy()" % (objName, objName)
        self.rotateBy(*args, **kwargs)

    def transform(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.transform()': use %s.transformBy()" % (objName, objName)
        self.transformBy(*args, **kwargs)

    def skew(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        print "Deprecated '%s.skew()': use %s.skewBy()" % (objName, objName)
        self.skewBy(*args, **kwargs)


# ==========
# = Point =
# ==========

class DeprecatedPoint(DeprecatedBase, DeprecatedTransformation):

    def select(self, state=True):
        print "Deprecated 'Point.select'"


# ==========
# = Anchor =
# ==========

class DeprecatedAnchor(DeprecatedBase, DeprecatedTransformation):

    def _get_position(self):
        print "Deprecated 'Anchor.position': use Anchor.x, Anchor.y"
        return self.x, self.y

    def _set_position(self, position):
        print "Deprecated 'Anchor.position': use Anchor.x, Anchor.y"
        x, y = position
        self.x = x
        self.y = y

    position = property(_get_position, _set_position, doc="Deprecated Anchor.position")

    def draw(self, pen):
        print "Deprecated 'Anchor.draw': UFO3 is not drawing anchors into pens"

    def drawPoints(self, pen):
            print "Deprecated 'Anchor.drawPoints': UFO3 is not drawing anchors into point pens"


# =============
# = Component =
# =============

class DeprecatedComponent(DeprecatedBase, DeprecatedTransformation):

    def _get_box(self):
        print "Deprecated 'Component.box': use Component.bounds"
        return self.bounds

    box = property(_get_box, doc="Deprecated Component.box")


# ===========
# = Segment =
# ===========

class DeprecatedSegment(DeprecatedBase, DeprecatedTransformation):

    def insertPoint(self, point):
        print "Deprecated Segment.insertPoint()"

    def removePoint(self, point):
        print "Deprecated Segment.removePoint()"


# ===========
# = Contour =
# ===========

class DeprecatedContour(DeprecatedBase, DeprecatedTransformation):

    def _get_box(self):
        print "Deprecated 'Contour.box': use Contour.bounds"
        return self.bounds

    box = property(_get_box, doc="Deprecated Contour.box")

    def reverseContour(self):
        print "Deprecated 'Contour.reverseContour()': use 'Contour.reverse()'"
        self.reverse()


# =========
# = Glyph =
# =========

class DeprecatedGlyph(DeprecatedBase, DeprecatedTransformation):

    def _get_box(self):
        print "Deprecated 'Glyph.box': use Glyph.bounds"
        return self.bounds

    box = property(_get_box, doc="Deprecated Glyph.box")

    def getAnchors(self):
        print "Deprecated 'Glyph.getAnchors()': use Glyph.anchors"
        return self.anchors

    def getComponents(self):
        print "Deprecated 'Glyph.getComponents()': use Glyph.components"
        return self.components

    def center(self, padding=None):
        print "Deprecated 'Glyph.center()'"

    def clearVGuides(self):
        print "Deprecated 'Glyph.clearVGuides()': use Glyph.clearGuidelines()"

    def clearHGuides(self):
        print "Deprecated 'Glyph.clearHGuides()': use Glyph.clearGuidelines()"


# =======
# = Lib =
# =======

class DeprecatedLib(DeprecatedBase):

    pass


# ==========
# = Groups =
# ==========

class DeprecatedGroups(DeprecatedBase):

    pass


# ===========
# = Kerning =
# ===========

class DeprecatedKerning(DeprecatedTransformation):

    def setParent(self, parent):
        print "Deprecated 'Kerning.setParent()'"

    def setChanged(self):
        print "Deprecated 'Kerning.setChanged': use Kerning.changed()"
        self.changed()

    def swapNames(self, swaptable):
        print "Deprecated Kerning.swapNames()"

    def getLeft(self, glyphName):
        print "Deprecated Kerning.getLeft()"

    def getRight(self, glyphName):
        print "Deprecated Kerning.getRight()"

    def getExtremes(self):
        print "Deprecated Kerning.getExtremes()"

    def add(self, value):
        print "Deprecated Kerning.self()"

    def minimize(self, minimum=10):
        print "Deprecated Kerning.minimize()"

    def importAFM(self, path, clearExisting=True):
        print "Deprecated Kerning.importAFM()"

    def getAverage(self):
        print "Deprecated Kerning.getAverage()"

    def combine(self, kerningDicts, overwriteExisting=True):
        print "Deprecated Kerning.combine()"

    def eliminate(self, leftGlyphsToEliminate=None, rightGlyphsToEliminate=None, analyzeOnly=False):
        print "Deprecated Kerning.eliminate()"

    def occurrenceCount(self, glyphsToCount):
        print "Deprecated Kerning.occurrenceCount()"

    def implodeClasses(self, leftClassDict=None, rightClassDict=None, analyzeOnly=False):
        print "Deprecated Kerning.implodeClasses()"

    def explodeClasses(self, leftClassDict=None, rightClassDict=None, analyzeOnly=False):
        print "Deprecated Kerning.explodeClasses()"


# ========
# = Info =
# ========

class DeprecatedInfo(DeprecatedBase):

    pass


# ============
# = Features =
# ============

class DeprecatedFeatures(DeprecatedBase):

    def round(self):
        print "Deprecated 'Feature.round()'"


# ========
# = Font =
# ========

class DeprecatedFont(DeprecatedBase):

    def getParent(self):
        print "Deprecated 'Font.getParent()'"

    def _get_fileName(self):
        print "Deprecated 'Font.fileName': use os.path.basename(Font.path)"
        return self.bounds

    _get_fileName = property(_get_fileName, doc="Deprecated Font.fileName")

    def generateGlyph(self, *args, **kwargs):
        print "Deprecated 'Font.generateGlyph()'"

    def compileGlyph(self, *args, **kwargs):
        print "Deprecated 'Font.compileGlyph()'"

    def getWidth(self, glyphName):
        print "Deprecated 'Font.getWidth(): use Font[glyphName].width'"
        return self[glyphName].width

    def getGlyph(self, glyphName):
        print "Deprecated 'Font.getGlyph(): use Font[glyphName]'"
        return self[glyphName]

    def getReverseComponentMapping(self):
        """
        Todo:
        * move this to layer as this is actually a very usefull method.
        """
        print "Deprecated 'Font.getReverseComponentMapping()'"

    def getCharacterMapping(self):
        """
        Todo:
        * move this to layer as this is actually a very usefull method.
        """
        print "Deprecated 'Font.getCharacterMapping()'"

    def getGlyphNameToFileNameFunc(self):
        print "Deprecated 'Font.getGlyphNameToFileNameFunc()'"



