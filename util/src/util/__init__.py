from colorzero.color import Color


def invert_lightness(color: Color|str) -> Color|str:
    match color:
        case Color():
            return _invert_lightness(color)
        case str():
            # Split into RGB and optional alpha components
            rgb, alpha = (color[:-2], color[-2:]) if len(color) == 9 else (color, "")
            return _invert_lightness(Color.from_string(rgb)).html + alpha


def _invert_lightness(color: Color) -> Color:
    orig_hls = color.hls
    return Color.from_hls(h=orig_hls.h, l=1 - orig_hls.l, s=orig_hls.s)
    