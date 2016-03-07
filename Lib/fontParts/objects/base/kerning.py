from base import BaseDict


class BaseKerning(BaseObject):


    def __repr__(self):
        pass
        
    remove = __delitem__ # RoboFab had remove, but not __dellitem__

    def asDict(self, returnIntegers=True):
        """
        Return this object as a regular dictionary.

        XXX what does returnIntegers do? is it needed?
        """

    # ---------------
    # Math Operations
    # ---------------

    def add(self, value):
        """
        Add value to all kerning pairs.
        """
        
    def scale(self, value):
        """
        Scale all kernng pairs by value.
        """
    
    def round(self, multiple=10):
        """
        Round the kerning pair values to increments of multiple.

        XXX should multiple default to 1?
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, minKerning, maxKerning, value, clearExisting=True):
        """
        Interpolate all pairs between minKerning and maxKerning.
        The interpolation occurs on a 0 to 1.0 range where minKerning
        is located at 0 and maxKerning is located at 1.0.

        factor is the interpolation value. It may be less than 0
        and greater than 1.0.

        clearExisting will clear existing kerning before interpolating.
        """

    # ------------------
    # Questionable Stuff
    # ------------------

    def getAverage(self):
        """
        return average of all kerning pairs

        XXX needed?
        """

    def getExtremes(self):
        """
        return the lowest and highest kerning values

        XXX needed?
        """
            
    def minimize(self, minimum=10):
        """
        eliminate pairs with value less than minimum

        XXX needed?
        """
    
    def eliminate(self, leftGlyphsToEliminate=None, rightGlyphsToEliminate=None, analyzeOnly=False):
        """
        eliminate pairs containing a left glyph that is in the leftGlyphsToEliminate list
        or a right glyph that is in the rightGlyphsToELiminate list.
        sideGlyphsToEliminate can be a string: 'a' or list: ['a', 'b'].
        analyzeOnly will not remove pairs. it will return a count
        of all pairs that would be removed.
        """
    
    def occurrenceCount(self, glyphsToCount):
        """
        return a dict with glyphs as keys and the number of 
        occurances of that glyph in the kerning pairs as the value
        glyphsToCount can be a string: 'a' or list: ['a', 'b']

        XXX needed?
        """
    
    def getLeft(self, glyphName):
        """
        Return a list of kerns with glyphName as left character.

        XXX needed?
        """
                
    def getRight(self, glyphName):
        """
        Return a list of kerns with glyphName as left character.

        XXX needed?
        """
        
    def combine(self, kerningDicts, overwriteExisting=True):
        """
        combine two or more kerning dictionaries.
        overwrite exsisting duplicate pairs if overwriteExisting=True

        XXX needed?
        """
                    
    def swapNames(self, swapTable):
        """
        change glyph names in all kerning pairs based on swapTable.
        swapTable = {'BeforeName':'AfterName', ...}

        XXX needed?
        """
                
    def explodeClasses(self, leftClassDict=None, rightClassDict=None, analyzeOnly=False):
        """
        turn class kerns into real kerning pairs. classes should
        be defined in dicts: {'O':['C', 'G', 'Q'], 'H':['B', 'D', 'E', 'F', 'I']}.
        analyzeOnly will not remove pairs. it will return a count
        of all pairs that would be added

        XXX needed?
        """
                    
    def implodeClasses(self, leftClassDict=None, rightClassDict=None, analyzeOnly=False):
        """
        condense the number of kerning pairs by applying classes.
        this will eliminate all pairs containg the classed glyphs leaving
        pairs that contain the key glyphs behind. analyzeOnly will not
        remove pairs. it will return a count of all pairs that would be removed.

        XXX needed?
        """
        
    def importAFM(self, path, clearExisting=True):
        """
        Import kerning pairs from an AFM file. clearExisting=True will
        clear all exising kerning

        XXX needed?
        """