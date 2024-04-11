-------------------------------
EnvGratingComponent
-------------------------------
A class for presenting grating stimuli

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
=================

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

`Anchor`
    Which point on the stimulus should be anchored to its exact position?
    
    Options:
    - center
    - top-center
    - bottom-center
    - center-left
    - center-right
    - top-left
    - top-right
    - bottom-left
    - bottom-right

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

`OpenGL blend mode`
    OpenGL Blendmode. Avg is most common mode in PsychoPy, add is useful if combining a beat with the carrier image or numpy array at point of display
    
    Options:
    - avg
    - add

Carrier
=================

`Carrier contrast`
    Contrast of background carrier

`Orientation`
    Orientation of this stimulus (in deg)
    
    Options:
    - -360
    - 360

`Carrier texture`
    The (2D) texture of the background - can be sin, sqr, sinXsin... or a filename (including path)
    
    Options:
    - sin
    - sqr
    - sinXsin

`Mask`
    An image to define the alpha mask (ie shape)- gauss, circle... or a filename (including path)
    
    Options:
    - gauss
    - circle

`Carrier spatial frequency`
    Spatial frequency of background carrier repeats across the grating in 1 or 2 dimensions, e.g. 4 or [2,3]

`Carrier phase (in cycles)`
    Spatial positioning of the background carrier (wraps in range 0-1.0)

`Texture resolution`
    Resolution of the texture for standard ones such as sin, sqr etc. For most cases a value of 256 pixels will suffice
    
    Options:
    - 32
    - 64
    - 128
    - 256
    - 512

`Interpolate`
    How should the image be interpolated if/when rescaled
    
    Options:
    - linear
    - nearest

Envelope
=================

`Envelope texture`
    The (2D) texture of the envelope - can be sin, sqr, sinXsin... or a filename (including path)
    
    Options:
    - sin
    - sqr
    - sinXsin

`Envelope spatial frequency`
    Spatial frequency of the modulation envelope repeats across the grating in 1 or 2 dimensions, e.g. 4 or [2,3]

`Envelope phase`
    Spatial positioning of the modulation envelope(wraps in range 0-1.0)

`Envelope orientation`
    Orientation of the modulation envelope(wraps in range 0-360)

`Envelope modulation depth`
    Modulation depth of modulation envelope

`Power to which envelope is raised`
    Power of modulation envelope. The modulator will be raised to this power according to the equation S=cC*(1+mM)^power, where C is the carrier and M is the modulator. and c and m are there respective contrast and modulation depth. Only works with AM envelopes (hence +1) in equation. Power is ignored if a beat is requested. This is used to obtain the square root of the modulator (power = 0.5) which is useful if combining two envelope gratings with different carriers and a 180 degree phase shift as the resulting combined signal will not have any reduction in local contrast at any point in the image. This is similar - but not identical to - the method used by Landy and Oruc, Vis Res 2002. Note overall contrast (apparent carrier contrast) will be altered.

`Is modulation a beat`
    Do you want a 'beat'? [beat = carrier*envelope, no beat = carrier*(1+envelope), True/False, Y/N]

