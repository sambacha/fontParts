.. highlight:: python
.. module:: fontParts.objects.base

##############
Object Methods
##############

Font
****

Must Override
-------------
.. automethod:: BaseFont._close
.. automethod:: BaseFont._generate
.. automethod:: BaseFont._getGuideline
.. automethod:: BaseFont._get_defaultLayer
.. automethod:: BaseFont._get_features
.. automethod:: BaseFont._get_glyphOrder
.. automethod:: BaseFont._get_groups
.. automethod:: BaseFont._get_info
.. automethod:: BaseFont._get_kerning
.. automethod:: BaseFont._get_layerOrder
.. automethod:: BaseFont._get_layers
.. automethod:: BaseFont._get_lib
.. automethod:: BaseFont._get_path
.. automethod:: BaseFont._init
.. automethod:: BaseFont._lenGuidelines
.. automethod:: BaseFont._newLayer
.. automethod:: BaseFont._removeGuideline
.. automethod:: BaseFont._removeLayer
.. automethod:: BaseFont._save
.. automethod:: BaseFont._set_defaultLayer
.. automethod:: BaseFont._set_glyphOrder
.. automethod:: BaseFont._set_layerOrder

May Override
------------
.. automethod:: BaseFont._appendGuideline
.. automethod:: BaseFont._autoUnicodes
.. automethod:: BaseFont._clearGuidelines
.. automethod:: BaseFont._contains
.. automethod:: BaseFont._getItem
.. automethod:: BaseFont._getLayer
.. automethod:: BaseFont._get_guidelines
.. automethod:: BaseFont._insertGlyph
.. automethod:: BaseFont._interpolate
.. automethod:: BaseFont._isCompatible
.. automethod:: BaseFont._iter
.. automethod:: BaseFont._keys
.. automethod:: BaseFont._len
.. automethod:: BaseFont._newGlyph
.. automethod:: BaseFont._removeGlyph
.. automethod:: BaseFont._round

Info
****

Must Override
-------------

May Override
------------
.. automethod:: BaseInfo._getAttr
.. automethod:: BaseInfo._init
.. automethod:: BaseInfo._interpolate
.. automethod:: BaseInfo._round
.. automethod:: BaseInfo._setAttr
.. automethod:: BaseInfo.copyData

Groups
******

Must Override
-------------
.. automethod:: BaseGroups._contains
.. automethod:: BaseGroups._delItem
.. automethod:: BaseGroups._getItem
.. automethod:: BaseGroups._items
.. automethod:: BaseGroups._setItem

May Override
------------
.. automethod:: BaseGroups._clear
.. automethod:: BaseGroups._findGlyph
.. automethod:: BaseGroups._get
.. automethod:: BaseGroups._init
.. automethod:: BaseGroups._iter
.. automethod:: BaseGroups._keys
.. automethod:: BaseGroups._len
.. automethod:: BaseGroups._pop
.. automethod:: BaseGroups._update
.. automethod:: BaseGroups._values

Kerning
*******

Must Override
-------------
.. automethod:: BaseKerning._contains
.. automethod:: BaseKerning._delItem
.. automethod:: BaseKerning._getItem
.. automethod:: BaseKerning._items
.. automethod:: BaseKerning._setItem

May Override
------------
.. automethod:: BaseKerning._clear
.. automethod:: BaseKerning._get
.. automethod:: BaseKerning._init
.. automethod:: BaseKerning._interpolate
.. automethod:: BaseKerning._iter
.. automethod:: BaseKerning._keys
.. automethod:: BaseKerning._len
.. automethod:: BaseKerning._pop
.. automethod:: BaseKerning._round
.. automethod:: BaseKerning._scale
.. automethod:: BaseKerning._update
.. automethod:: BaseKerning._values

Features
********

Must Override
-------------
.. automethod:: BaseFeatures._get_text
.. automethod:: BaseFeatures._set_text

May Override
------------
.. automethod:: BaseFeatures._init
.. automethod:: BaseFeatures.copyData

Lib
***

Must Override
-------------
.. automethod:: BaseLib._contains
.. automethod:: BaseLib._delItem
.. automethod:: BaseLib._getItem
.. automethod:: BaseLib._items
.. automethod:: BaseLib._setItem

May Override
------------
.. automethod:: BaseLib._clear
.. automethod:: BaseLib._get
.. automethod:: BaseLib._init
.. automethod:: BaseLib._iter
.. automethod:: BaseLib._keys
.. automethod:: BaseLib._len
.. automethod:: BaseLib._pop
.. automethod:: BaseLib._update
.. automethod:: BaseLib._values

Layer
*****

Must Override
-------------
.. automethod:: BaseLayer._getItem
.. automethod:: BaseLayer._get_color
.. automethod:: BaseLayer._get_lib
.. automethod:: BaseLayer._get_name
.. automethod:: BaseLayer._keys
.. automethod:: BaseLayer._newGlyph
.. automethod:: BaseLayer._removeGlyph
.. automethod:: BaseLayer._set_color
.. automethod:: BaseLayer._set_name

May Override
------------
.. automethod:: BaseLayer._autoUnicodes
.. automethod:: BaseLayer._contains
.. automethod:: BaseLayer._init
.. automethod:: BaseLayer._insertGlyph
.. automethod:: BaseLayer._interpolate
.. automethod:: BaseLayer._isCompatible
.. automethod:: BaseLayer._iter
.. automethod:: BaseLayer._len
.. automethod:: BaseLayer._round

Glyph
*****

Must Override
-------------
.. automethod:: BaseGlyph._addImage
.. automethod:: BaseGlyph._autoUnicodes
.. automethod:: BaseGlyph._clearImage
.. automethod:: BaseGlyph._getAnchor
.. automethod:: BaseGlyph._getComponent
.. automethod:: BaseGlyph._getContour
.. automethod:: BaseGlyph._getGuideline
.. automethod:: BaseGlyph._get_height
.. automethod:: BaseGlyph._get_image
.. automethod:: BaseGlyph._get_lib
.. automethod:: BaseGlyph._get_markColor
.. automethod:: BaseGlyph._get_name
.. automethod:: BaseGlyph._get_note
.. automethod:: BaseGlyph._get_unicodes
.. automethod:: BaseGlyph._get_width
.. automethod:: BaseGlyph._lenAnchors
.. automethod:: BaseGlyph._lenComponents
.. automethod:: BaseGlyph._lenContours
.. automethod:: BaseGlyph._lenGuidelines
.. automethod:: BaseGlyph._newLayer
.. automethod:: BaseGlyph._removeAnchor
.. automethod:: BaseGlyph._removeComponent
.. automethod:: BaseGlyph._removeContour
.. automethod:: BaseGlyph._removeGuideline
.. automethod:: BaseGlyph._removeOverlap
.. automethod:: BaseGlyph._set_height
.. automethod:: BaseGlyph._set_markColor
.. automethod:: BaseGlyph._set_name
.. automethod:: BaseGlyph._set_note
.. automethod:: BaseGlyph._set_unicodes
.. automethod:: BaseGlyph._set_width

May Override
------------
.. automethod:: BaseGlyph.__add__
.. automethod:: BaseGlyph.__div__
.. automethod:: BaseGlyph.__mul__
.. automethod:: BaseGlyph.__rmul__
.. automethod:: BaseGlyph.__sub__
.. automethod:: BaseGlyph._appendAnchor
.. automethod:: BaseGlyph._appendComponent
.. automethod:: BaseGlyph._appendContour
.. automethod:: BaseGlyph._appendGlyph
.. automethod:: BaseGlyph._appendGuideline
.. automethod:: BaseGlyph._clear
.. automethod:: BaseGlyph._clearAnchors
.. automethod:: BaseGlyph._clearComponents
.. automethod:: BaseGlyph._clearContours
.. automethod:: BaseGlyph._clearGuidelines
.. automethod:: BaseGlyph._decompose
.. automethod:: BaseGlyph._getLayer
.. automethod:: BaseGlyph._get_anchors
.. automethod:: BaseGlyph._get_bottomMargin
.. automethod:: BaseGlyph._get_bounds
.. automethod:: BaseGlyph._get_components
.. automethod:: BaseGlyph._get_contours
.. automethod:: BaseGlyph._get_guidelines
.. automethod:: BaseGlyph._get_leftMargin
.. automethod:: BaseGlyph._get_rightMargin
.. automethod:: BaseGlyph._get_topMargin
.. automethod:: BaseGlyph._get_unicode
.. automethod:: BaseGlyph._init
.. automethod:: BaseGlyph._interpolate
.. automethod:: BaseGlyph._isCompatible
.. automethod:: BaseGlyph._iterContours
.. automethod:: BaseGlyph._moveBy
.. automethod:: BaseGlyph._pointInside
.. automethod:: BaseGlyph._removeLayer
.. automethod:: BaseGlyph._rotateBy
.. automethod:: BaseGlyph._round
.. automethod:: BaseGlyph._scaleBy
.. automethod:: BaseGlyph._set_bottomMargin
.. automethod:: BaseGlyph._set_leftMargin
.. automethod:: BaseGlyph._set_rightMargin
.. automethod:: BaseGlyph._set_topMargin
.. automethod:: BaseGlyph._set_unicode
.. automethod:: BaseGlyph._skewBy
.. automethod:: BaseGlyph._transformBy

Contour
*******

Must Override
-------------
.. automethod:: BaseContour._getPoint
.. automethod:: BaseContour._get_clockwise
.. automethod:: BaseContour._get_identifier
.. automethod:: BaseContour._insertPoint
.. automethod:: BaseContour._lenPoints
.. automethod:: BaseContour._removePoint
.. automethod:: BaseContour._set_index

May Override
------------
.. automethod:: BaseContour._appendBPoint
.. automethod:: BaseContour._appendSegment
.. automethod:: BaseContour._autoStartSegment
.. automethod:: BaseContour._draw
.. automethod:: BaseContour._drawPoints
.. automethod:: BaseContour._get_bounds
.. automethod:: BaseContour._get_index
.. automethod:: BaseContour._get_points
.. automethod:: BaseContour._get_segments
.. automethod:: BaseContour._init
.. automethod:: BaseContour._insertBPoint
.. automethod:: BaseContour._insertSegment
.. automethod:: BaseContour._len__segments
.. automethod:: BaseContour._moveBy
.. automethod:: BaseContour._pointInside
.. automethod:: BaseContour._removeSegment
.. automethod:: BaseContour._reverse
.. automethod:: BaseContour._rotateBy
.. automethod:: BaseContour._round
.. automethod:: BaseContour._scaleBy
.. automethod:: BaseContour._setStartSegment
.. automethod:: BaseContour._set_clockwise
.. automethod:: BaseContour._skewBy
.. automethod:: BaseContour._transformBy

Segment
*******

Must Override
-------------

May Override
------------
.. automethod:: BaseSegment._getItem
.. automethod:: BaseSegment._get_base_offCurve
.. automethod:: BaseSegment._get_index
.. automethod:: BaseSegment._get_offCurve
.. automethod:: BaseSegment._get_onCurve
.. automethod:: BaseSegment._get_points
.. automethod:: BaseSegment._get_smooth
.. automethod:: BaseSegment._get_type
.. automethod:: BaseSegment._init
.. automethod:: BaseSegment._iterPoints
.. automethod:: BaseSegment._len
.. automethod:: BaseSegment._moveBy
.. automethod:: BaseSegment._rotateBy
.. automethod:: BaseSegment._scaleBy
.. automethod:: BaseSegment._set_smooth
.. automethod:: BaseSegment._set_type
.. automethod:: BaseSegment._skewBy
.. automethod:: BaseSegment._transformBy
.. automethod:: BaseSegment.copyData

BPoint
******

Must Override
-------------

May Override
------------
.. automethod:: BaseBPoint._get_anchor
.. automethod:: BaseBPoint._get_bcpIn
.. automethod:: BaseBPoint._get_bcpOut
.. automethod:: BaseBPoint._get_index
.. automethod:: BaseBPoint._get_type
.. automethod:: BaseBPoint._init
.. automethod:: BaseBPoint._moveBy
.. automethod:: BaseBPoint._rotateBy
.. automethod:: BaseBPoint._scaleBy
.. automethod:: BaseBPoint._set_anchor
.. automethod:: BaseBPoint._set_bcpIn
.. automethod:: BaseBPoint._set_bcpOut
.. automethod:: BaseBPoint._set_type
.. automethod:: BaseBPoint._skewBy
.. automethod:: BaseBPoint._transformBy
.. automethod:: BaseBPoint.copyData

Point
*****

Must Override
-------------
.. automethod:: BasePoint._get_identifier
.. automethod:: BasePoint._get_name
.. automethod:: BasePoint._get_smooth
.. automethod:: BasePoint._get_type
.. automethod:: BasePoint._get_x
.. automethod:: BasePoint._get_y
.. automethod:: BasePoint._set_name
.. automethod:: BasePoint._set_smooth
.. automethod:: BasePoint._set_type
.. automethod:: BasePoint._set_x
.. automethod:: BasePoint._set_y

May Override
------------
.. automethod:: BasePoint._get_index
.. automethod:: BasePoint._init
.. automethod:: BasePoint._moveBy
.. automethod:: BasePoint._rotateBy
.. automethod:: BasePoint._round
.. automethod:: BasePoint._scaleBy
.. automethod:: BasePoint._skewBy
.. automethod:: BasePoint._transformBy
.. automethod:: BasePoint.copyData

Component
*********

Must Override
-------------
.. automethod:: BaseComponent._decompose
.. automethod:: BaseComponent._get_baseGlyph
.. automethod:: BaseComponent._get_identifier
.. automethod:: BaseComponent._get_transformation
.. automethod:: BaseComponent._set_baseGlyph
.. automethod:: BaseComponent._set_index
.. automethod:: BaseComponent._set_transformation

May Override
------------
.. automethod:: BaseComponent._draw
.. automethod:: BaseComponent._drawPoints
.. automethod:: BaseComponent._get_bounds
.. automethod:: BaseComponent._get_index
.. automethod:: BaseComponent._get_offset
.. automethod:: BaseComponent._get_scale
.. automethod:: BaseComponent._init
.. automethod:: BaseComponent._moveBy
.. automethod:: BaseComponent._pointInside
.. automethod:: BaseComponent._rotateBy
.. automethod:: BaseComponent._round
.. automethod:: BaseComponent._scaleBy
.. automethod:: BaseComponent._set_offset
.. automethod:: BaseComponent._set_scale
.. automethod:: BaseComponent._skewBy
.. automethod:: BaseComponent._transformBy
.. automethod:: BaseComponent.copyData

Anchor
******

Must Override
-------------
.. automethod:: BaseAnchor._get_color
.. automethod:: BaseAnchor._get_identifier
.. automethod:: BaseAnchor._get_name
.. automethod:: BaseAnchor._get_x
.. automethod:: BaseAnchor._get_y
.. automethod:: BaseAnchor._set_color
.. automethod:: BaseAnchor._set_name
.. automethod:: BaseAnchor._set_x
.. automethod:: BaseAnchor._set_y

May Override
------------
.. automethod:: BaseAnchor._init
.. automethod:: BaseAnchor._moveBy
.. automethod:: BaseAnchor._rotateBy
.. automethod:: BaseAnchor._scaleBy
.. automethod:: BaseAnchor._skewBy
.. automethod:: BaseAnchor._transformBy
.. automethod:: BaseAnchor.copyData

Image
*****

Must Override
-------------
.. automethod:: BaseImage._get_color
.. automethod:: BaseImage._get_data
.. automethod:: BaseImage._get_transformation
.. automethod:: BaseImage._set_color
.. automethod:: BaseImage._set_data
.. automethod:: BaseImage._set_transformation

May Override
------------
.. automethod:: BaseImage._get_offset
.. automethod:: BaseImage._get_scale
.. automethod:: BaseImage._init
.. automethod:: BaseImage._moveBy
.. automethod:: BaseImage._rotateBy
.. automethod:: BaseImage._round
.. automethod:: BaseImage._scaleBy
.. automethod:: BaseImage._set_offset
.. automethod:: BaseImage._set_scale
.. automethod:: BaseImage._skewBy
.. automethod:: BaseImage._transformBy
.. automethod:: BaseImage.copyData

Guideline
*********

Must Override
-------------
.. automethod:: BaseGuideline._get_angle
.. automethod:: BaseGuideline._get_color
.. automethod:: BaseGuideline._get_identifier
.. automethod:: BaseGuideline._get_name
.. automethod:: BaseGuideline._get_x
.. automethod:: BaseGuideline._get_y
.. automethod:: BaseGuideline._set_angle
.. automethod:: BaseGuideline._set_color
.. automethod:: BaseGuideline._set_name
.. automethod:: BaseGuideline._set_x
.. automethod:: BaseGuideline._set_y

May Override
------------
.. automethod:: BaseGuideline._get_index
.. automethod:: BaseGuideline._init
.. automethod:: BaseGuideline._moveBy
.. automethod:: BaseGuideline._rotateBy
.. automethod:: BaseGuideline._round
.. automethod:: BaseGuideline._scaleBy
.. automethod:: BaseGuideline._skewBy
.. automethod:: BaseGuideline._transformBy
.. automethod:: BaseGuideline.copyData
