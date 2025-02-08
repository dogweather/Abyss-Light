from colorzero.color import Color
from util import invert_lightness, _invert_lightness

DARK     = Color.from_hls(h=100, l=0.2, s=0.8)
LIGHT    = Color.from_hls(h=100, l=0.8, s=0.8)
FULL_RED = Color.from_rgb(r=1, g=0, b=0)

DARK_RGBA  = "#0063a5dd"
LIGHT_RGBA = "#5abdffdd"

DARK_RGB  = "#0063a5"
LIGHT_RGB = "#5abdff"

def test_dark_to_light():
    assert _invert_lightness(DARK).html == LIGHT.html

def test_light_to_dark():
    assert _invert_lightness(LIGHT).html == DARK.html

def test_full_red_does_not_change():
    assert _invert_lightness(FULL_RED).html == FULL_RED.html

# RGB

def test_dark_to_light_rgb():
    assert invert_lightness(DARK_RGB) == LIGHT_RGB

def test_light_to_dark_rgb():
    assert invert_lightness(LIGHT_RGB) == DARK_RGB

# RGBA

def test_dark_to_light_rgba():
    assert invert_lightness(DARK_RGBA) == LIGHT_RGBA

def test_light_to_dark_rgba():
    assert invert_lightness(LIGHT_RGBA) == DARK_RGBA
