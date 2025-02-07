from colorzero.color import Color


def invert_lightness(color: Color|str) -> Color:
    match color:
        case Color():
            orig_hls = color.hls
        case str():
            orig_hls = Color.from_string(color).hls
        case _:
            raise ValueError(f"Invalid color: {color}")

    return Color.from_hls(h=orig_hls.h, l=1 - orig_hls.l, s=orig_hls.s)
