from colorzero.color import Color
from util import invert_lightness

DARK  = Color.from_hls(h=100, l=0.2, s=0.8)
LIGHT = Color.from_hls(h=100, l=0.8, s=0.8)
FULL_RED = Color.from_rgb(r=1, g=0, b=0)
    

def test_make_dark_light():
    assert invert_lightness(DARK).html == LIGHT.html


def test_make_light_dark():
    assert invert_lightness(LIGHT).html == DARK.html


def test_full_red_does_not_change():
    assert invert_lightness(FULL_RED).html == FULL_RED.html
