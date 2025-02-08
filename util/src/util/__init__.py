from colorzero.color import Color


def invert_lightness(color: Color|str) -> Color|str:
    match color:
        case Color():
            return _invert_lightness(color)
        case str():
            return _invert_lightness(Color.from_string(color)).html
        case _:
            raise ValueError(f"Invalid color: {color}")


def _invert_lightness(color: Color) -> Color:
    orig_hls = color.hls
    return Color.from_hls(h=orig_hls.h, l=1 - orig_hls.l, s=orig_hls.s)
