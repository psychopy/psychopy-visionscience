-------------------------------
NoiseStimComponent
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

`Type of noise`
    Type of noise (Binary, Normal, Gabor, Isotropic, White, Coloured, Filtered, Image)
    
    Options:
    - Binary
    - Normal
    - Uniform
    - Gabor
    - Isotropic
    - White
    - Filtered
    - Image

`Radomize image component`
    Which image component should be randomised? [Amplitude,Phase]. Randomizing amplitude will keep the phase spectrum of the image but set the amplitude spectrum to random values [0...1]. This keeps spatial structure in tact. Randoming the phase spectrum will keep the amplitude spectrum of the image  but set the phase spectrum to random values [-pi...pi] in radians. This makes a noise sample with no obvious structure. 
    
    Options:
    - Phase
    - Amplitude

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

`Orientation`
    Orientation of this stimulus (in deg)
    
    Options:
    - -360
    - 360

`Noise element size`
    (Binary, Normal and Uniform only) Size of noise elements in the stimulus units, for pixelated noise.

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
    OpenGL Blendmode [avg, add (avg is most common mode in PsychoPy, add is used if you want to generate the sum of two components)]
    
    Options:
    - avg
    - add

Texture
=================

`Contrast`
    Michaelson contrast of the image

`Image from which to derive noise spectrum`
    An image from which to derive the frequency spectrum for the noise. Give filename (including path)

`Mask`
    An image to define the alpha mask (ie shape)- gauss, circle... or a filename (including path)

`Final spatial frequency`
    Final spatial frequency of image in 1 or 2 dimensions, e.g. 4 or [2,3]. Use None to set to 1 copy of noise per unit length of image or 1 copy of noise per image if units=pix. Set to 1/size (or [1/size,1/size]) where size is a number (or variable) equal to the size of the stimulus to get one copy of noise per image regardless of the units.

`Phase (in cycles)`
    Spatial positioning of the noise within the stimulus (wraps in range 0-1.0)

`Texture resolution`
    Resolution of the texture for standard ones such as sin, sqr etc. For most cases a value of 256 pixels will suffice
    
    Options:
    - 32
    - 64
    - 128
    - 256
    - 512
    - 1024

`Interpolate`
    How should the image be interpolated if/when rescaled
    
    Options:
    - linear
    - nearest

`Apply filter to noise sample`
    Apply filter to noise sample? [Butterworth, Gabor, Isoptopic]. A filter with parameters taken from the either the Filtered (Butterworth) or Gabor/Isotropic tab will be applied to OTHER noise types. [NOTE: if noise of the same type as the filter is requested the filter is applied, once only, to a white noise sample.]
    
    Options:
    - None
    - Butterworth
    - Gabor
    - Isotropic

`Base spatial frequency`
    Base spatial frequency in cycles per unit length If units = pix this value should be < 0.5.

`Spatial frequency bandwidth`
    Spatial frequency bandwidth in octaves - Full width half height

`Orientation bandwidth for Gabor noise`
    Orientation bandwidth in degrees (Gabor only) - Full width half height

`Orientation for Gabor filter`
    Orientation of Gabor filter in degrees. Used to set the orientation of a Gabor filter to be applied to another noise sample with a different overall orientation. The best way to set the orientation of a Gabor noise sample is to leave this as 0 degree and use the overall orientation on the Advanced tab to vary the dominant orientation of the noise. If using this setting for orientation it is strongly recommended to set the interpolation method to 'linear' on the Advanced tab to avoid pixelization.

`Skew in frequency spectrum`
    Exponent for the slope of the filter's amplitude spectrum (A=f^Exponent). 0 = flat, -1 = slope of 1/f. When used on its own the 'filtered' noise type applies the filter to white noise so the resulting noise samples have the spectral properties of the filter.  When filtering a noise sample of another type this term takes the original spectrum and multiplies it by a ramp in frequency space with values set by the exponent. It does not force the spectrum to a specific slope. 

`Order of filter`
    Order of filter - higher = steeper fall off, zero = no filter

`Upper cut off frequency`
    Upper cutoff frequency in cycles per unit length. Set very high to avoid an upper cutoff and make a high pass filter.

`Lower cut off frequency`
    Lower cutoff frequency in cycles per unit length. Set to zero to avoid a lower cuttoff and make a low pass filter.

`Number of standard deviations at which to clip noise`
    Truncate high and low values beyond stated standard deviations from mean and rescale greyscale range. This is not used at all for 'binary' or 'uniform' noise and scales rather than clips 'normal' noise). The higher this is the lower the final RMS contrast. If very low noise may appear binarised. NOTE: If a filter is used clipping and rescaling are applied after the filter, regardless of the noise type.

Timing
=================

`How to update noise sample`
    How to update noise if not otherwise required by other changes (none, repeat, N-frames, Seconds)
    
    Options:
    - None
    - Repeat
    - N-frames
    - Seconds

`When to update noise sample`
    How often to update noise (in frames or seconds) - can be a variable, ignored if any noise characteristic is updating on every frame

