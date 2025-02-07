from colorzero.color import Color


def invert_lightness(color: Color) -> Color:
    orig_hls = color.hls
    return Color.from_hls(h=orig_hls.h, l=1 - orig_hls.l, s=orig_hls.s)
