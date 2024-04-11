-------------------------------
RadialStimComponent
-------------------------------
A class for presenting radial stimuli

    **Categories:** Stimuli
    **Works in:** PsychoPy

Parameters
-------------------------------

Basic
=================

`Name`
    Name of this component (alphanumeric or _, no spaces)

`start type`
    How do you want to define your start point?
    
    Options:
    - time (s)
    - frame N
    - condition

`stop type`
    How do you want to define your end point?
    
    Options:
    - duration (s)
    - duration (frames)
    - time (s)
    - frame N
    - condition

`Start`
    When does the component start?

`Stop`
    When does the component end? (blank is endless)

`Expected start (s)`
    (Optional) expected start (s), purely for representing in the timeline

`Expected duration (s)`
    (Optional) expected duration (s), purely for representing in the timeline

Data

`Save onset/offset times`
    Store the onset/offset times in the data file (as well as in the log file).

`Sync timing with screen refresh`
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)

Testing
=================

`Disable component`
    Disable this component

Layout
=================

`Spatial Units`
    Units of dimensions for this stimulus
    
    Options:
    - from exp settings
    - deg
    - cm
    - pix
    - norm
    - height
    - degFlatPos
    - degFlat

`Position [x,y]`
    Position of this stimulus (e.g. [1,2] )

`Size [w,h]`
    Size of this stimulus (either a single value or x,y pair, e.g. 2.5, [1,2] 

`Orientation`
    Orientation of this stimulus (in deg)
    
    Options:
    - -360
    - 360

Appearance
=================

`Foreground Color`
    Foreground color of this stimulus (e.g. $[1,1,0], red )

`Color Space`
    In what format (color space) have you specified the colors? (rgb, dkl, lms, hsv)
    
    Options:
    - rgb
    - dkl
    - lms
    - hsv

`Opacity`
    Opacity of the stimulus (1=opaque, 0=fully transparent, 0.5=translucent). Leave blank for each color to have its own opacity (recommended if any color is None).

`Contrast`
    Contrast of the stimulus (1.0=unchanged contrast, 0.5=decrease contrast, 0.0=uniform/no contrast, -0.5=slightly inverted, -1.0=totally inverted)

Texture
=================

`Texture`
    The (2D) texture of the grating - can be sin, sqr, sqrXsqr. or a filename (including path)
    
    Options:
    - sin
    - sqr
    - sqrXsqr

`Mask`
    An image to define the alpha mask (ie shape)- gauss, circle... or a filename (including path)
    
    Options:
    - gauss
    - circle

`Radial Cycles`
    Number of texture cycles from centre to periphery, i.e. it controls the number of ‘rings’.

`Angular Cycles`
    Number of cycles going around the stimulus. i.e. it controls the number of ‘spokes’.

`Radial Phase`
    This is the phase of the texture from the centre to the perimeter of the stimulus (in radians). Can be used to drift concentric rings out/inwards.

`Angular Phase`
    This is akin to setting the orientation of the texture around the stimulus in radians. If possible, it is more efficient to rotate the stimulus using its ori setting instead.

`Visible Wedge`
    Determines visible range.

`Interpolate`
    How should the image be interpolated if/when rescaled
    
    Options:
    - linear
    - nearest

`Texture resolution`
    Resolution of the texture for standard ones such as sin, sqr etc. For most cases a value of 256 pixels will suffice
    
    Options:
    - 32
    - 64
    - 128
    - 256
    - 512

