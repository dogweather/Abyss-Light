import pytest

from colorzero.color import Color
from util import invert_lightness

DARK  = Color.from_hls(h=100, l=0.2, s=0.8)
LIGHT = Color.from_hls(h=100, l=0.8, s=0.8)
    

def test_make_dark_light():
    assert invert_lightness(DARK).html == LIGHT.html


def test_make_light_dark():
    assert invert_lightness(LIGHT).html == DARK.html
