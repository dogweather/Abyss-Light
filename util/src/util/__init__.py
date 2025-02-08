from colorzero.color import Color


def invert_lightness(color: str) -> str:
    """
    Invert the lightness of a color. Handle both RGB and RGBA colors.

    Examples:
        >>> invert_lightness('#000000')
        '#ffffff'
        >>> invert_lightness('#ffffff')
        '#000000'
        >>> invert_lightness('#00000000')
        '#ffffff00'
        >>> invert_lightness('#ffffff00')
        '#00000000'
    """
    rgb, alpha = (color[:-2], color[-2:]) if len(color) == 9 else (color, "")
    new_rgb    = _invert_lightness(Color.from_string(rgb)).html
    return new_rgb + alpha

def _invert_lightness(color: Color) -> Color:
    orig_hls = color.hls
    return Color.from_hls(h=orig_hls.h, l=1 - orig_hls.l, s=orig_hls.s)
    