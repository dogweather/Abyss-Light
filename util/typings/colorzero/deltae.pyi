"""
This type stub file was generated by pyright.
"""

"Defines the various algorithms for :meth:`Color.difference`."
def euclid(color1, color2): # -> float:
    """
    Calculates color difference as a simple `Euclidean distance`_ by treating
    the three components as spatial dimensions.

    .. note::

        This function will return considerably different values to the other
        difference functions. In particular, the maximum "difference" will be
        :math:`\\sqrt{3}` which is much smaller than the output of the CIE
        functions.

    .. _Euclidean distance: https://en.wikipedia.org/wiki/Euclidean_distance
    """
    ...

def cie1976(color1, color2): # -> float:
    """
    Calculates color difference according to the `CIE 1976`_ formula.
    Effectively this is the Euclidean formula, but with CIE L*a*b* components
    instead of RGB.

    .. _CIE 1976: https://en.wikipedia.org/wiki/Color_difference#CIE76
    """
    ...

def cie1994(color1, color2, method): # -> float:
    """
    Calculates color difference according to the `CIE 1994`_ formula. The
    *method* can be either "cie1994g" for the "graphical" biases, or "cie1994t"
    for the "textile" biases. The CIE1994 is also basically the Euclidean
    formula (with biases) but in CIE L*C*H* space.

    .. _CIE 1994: https://en.wikipedia.org/wiki/Color_difference#CIE94
    """
    ...

def cie1994g(color1, color2): # -> float:
    """
    Calculates color difference according to the `CIE 1994`_ formula with the
    "textile" bias. See :func:`cie1994` for further information.

    .. _CIE 1994: https://en.wikipedia.org/wiki/Color_difference#CIE94
    """
    ...

def cie1994t(color1, color2): # -> float:
    """
    Calculates color difference according to the `CIE 1994`_ formula with the
    "graphics" bias. See :func:`cie1994` for further information.

    .. _CIE 1994: https://en.wikipedia.org/wiki/Color_difference#CIE94
    """
    ...

def ciede2000(color1, color2): # -> float:
    """
    Calculates color difference according to the `CIEDE 2000`_ formula. This is
    the most accurate algorithm currently implemented but also the most complex
    and slowest. Like CIE1994 it is largely based in CIE L*C*h* space, but with
    several modifications to account for perceptual uniformity flaws.

    .. _CIEDE 2000: https://en.wikipedia.org/wiki/Color_difference#CIEDE2000
    """
    ...

