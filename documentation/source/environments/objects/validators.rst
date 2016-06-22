.. highlight:: python
.. module:: fontParts.base.validators

##########
Validators
##########

.. autofunction:: validatorFileFormatVersion

*******
Kerning
*******

.. autofunction:: validateKerningKey
.. autofunction:: validateKerningValue

******
Groups
******
.. autofunction:: validateGroupKey
.. autofunction:: validateGroupValue

********
Features
********

.. autofunction:: validateFeatureText

***
Lib
***

.. autofunction:: validateLibKey
.. autofunction:: validateLibValue

******
Layers
******

.. autofunction:: validateLayerOrder
.. autofunction:: validateDefaultLayer
.. autofunction:: validateLayerName

******
Glyphs
******

.. autofunction:: validateGlyphOrder

Identification
==============

.. autofunction:: validateGlyphName
.. autofunction:: validateGlyphUnicodes
.. autofunction:: validateGlyphUnicode

Metrics
=======

.. autofunction:: validateGlyphWidth
.. autofunction:: validateGlyphLeftMargin
.. autofunction:: validateGlyphRightMargin
.. autofunction:: validateGlyphHeight
.. autofunction:: validateGlyphBottomMargin
.. autofunction:: validateGlyphTopMargin

********
Contours
********

.. autofunction:: validateContourIndex
.. autofunction:: validateContour

******
Points
******

.. autofunction:: validatePointType
.. autofunction:: validatePointName

********
Segments
********

.. autofunction:: validateSegmentType

*******
BPoints
*******

.. autofunction:: validateBPointType

**********
Components
**********

.. autofunction:: validateComponentIndex

*******
Anchors
*******

.. autofunction:: validateAnchorIndex
.. autofunction:: validateAnchorName

****
Note
****

.. autofunction:: validateGlyphNote

**********
Guidelines
**********

.. autofunction:: validateGuidelineIndex
.. autofunction:: validateGuidelineAngle
.. autofunction:: validateGuidelineName

*******
Generic
*******

Positions
=========

.. autofunction:: validateX
.. autofunction:: validateY
.. autofunction:: validateCoordinateTuple
.. autofunction:: validateBoundingBox

Identification
==============

.. autofunction:: validateIndex
.. autofunction:: validateIdentifier
.. autofunction:: validateColor

Interpolation
=============

.. autofunction:: validateInterpolationFactor

Transformations
===============

.. autofunction:: validateTransformationMatrix
.. autofunction:: validateTransformationOffset
.. autofunction:: validateTransformationRotationAngle
.. autofunction:: validateTransformationSkewAngle
.. autofunction:: validateTransformationScale

Files
=====

.. autofunction:: validateFilePath

Standard
========

.. autofunction:: validateBoolean
