"""
This contains tons of cruft.
It's also very glyph+glyph centric.
"""

class BaseKerning(BaseObject):

    # needs all dict methods that make sense

    def __repr__(self):
        pass
            
    def __getitem__(self, key):
        pass
    
    def __setitem__(self, pair, value):
        pass
        
    def __len__(self):
        pass
    
    def keys(self):
        """
        return list of kerning pairs
        """
        
    def values(self):
        """
        return a list of kerning values
        """ 
    def items(self):
        """
        return a list of kerning items
        """
    
    def has_key(self, pair):
        pass
    
    def get(self, pair, default=None):
        """
        get a value. return None if the pair does not exist
        """
        
    def remove(self, pair):
        """
        remove a kerning pair
        """
    
    def getAverage(self):
        """
        return average of all kerning pairs
        """
    
    def getExtremes(self):
        """
        return the lowest and highest kerning values
        """
        
    def update(self, kerningDict):
        """
        replace kerning data with the data in the given kerningDict
        """
    
    def clear(self):
        """
        clear all kerning
        """
        
    def add(self, value):
        """
        add value to all kerning pairs
        """
        
    def scale(self, value):
        """
        scale all kernng pairs by value
        """
            
    def minimize(self, minimum=10):
        """
        eliminate pairs with value less than minimum
        """
    
    def eliminate(self, leftGlyphsToEliminate=None, rightGlyphsToEliminate=None, analyzeOnly=False):
        """
        eliminate pairs containing a left glyph that is in the leftGlyphsToEliminate list
        or a right glyph that is in the rightGlyphsToELiminate list.
        sideGlyphsToEliminate can be a string: 'a' or list: ['a', 'b'].
        analyzeOnly will not remove pairs. it will return a count
        of all pairs that would be removed.
        """
                
    def interpolate(self, sourceDictOne, sourceDictTwo, value, clearExisting=True):
        """
        interpolate the kerning between sourceDictOne
        and sourceDictTwo. clearExisting will clear existing
        kerning first.
        """
    
    def round(self, multiple=10):
        """
        round the kerning pair values to increments of multiple
        """
    
    def occurrenceCount(self, glyphsToCount):
        """
        return a dict with glyphs as keys and the number of 
        occurances of that glyph in the kerning pairs as the value
        glyphsToCount can be a string: 'a' or list: ['a', 'b']
        """
    
    def getLeft(self, glyphName):
        """
        Return a list of kerns with glyphName as left character.
        """
                
    def getRight(self, glyphName):
        """
        Return a list of kerns with glyphName as left character.
        """
        
    def combine(self, kerningDicts, overwriteExisting=True):
        """
        combine two or more kerning dictionaries.
        overwrite exsisting duplicate pairs if overwriteExisting=True
        """
                    
    def swapNames(self, swapTable):
        """
        change glyph names in all kerning pairs based on swapTable.
        swapTable = {'BeforeName':'AfterName', ...}
        """
                
    def explodeClasses(self, leftClassDict=None, rightClassDict=None, analyzeOnly=False):
        """
        turn class kerns into real kerning pairs. classes should
        be defined in dicts: {'O':['C', 'G', 'Q'], 'H':['B', 'D', 'E', 'F', 'I']}.
        analyzeOnly will not remove pairs. it will return a count
        of all pairs that would be added
        """
                    
    def implodeClasses(self, leftClassDict=None, rightClassDict=None, analyzeOnly=False):
        """
        condense the number of kerning pairs by applying classes.
        this will eliminate all pairs containg the classed glyphs leaving
        pairs that contain the key glyphs behind. analyzeOnly will not
        remove pairs. it will return a count of all pairs that would be removed.
        """
        
    def importAFM(self, path, clearExisting=True):
        """
        Import kerning pairs from an AFM file. clearExisting=True will
        clear all exising kerning
        """
                
    def asDict(self, returnIntegers=True):
        """
        return the object as a dictionary
        """
