from fontParts.test import testEnvironment
from fontParts.nonelab.font import RFont
from fontParts.nonelab.glyph import RGlyph
from fontParts.nonelab.anchor import RAnchor

classMapping = dict(
    font=RFont,
    glyph=RGlyph,
    anchor=RAnchor
)

def noneLabObjectGenerator(cls):
    return classMapping[cls]()

if __name__ == "__main__":
    testEnvironment(noneLabObjectGenerator)