import pytest

from colorzero.color import Color
from util import invert_lightness


def test_make_dark_light():
    dark_color  = Color.from_hls(h=100, l=0.2, s=0.8)
    light_color = Color.from_hls(h=100, l=0.8, s=0.8)
    
    assert invert_lightness(dark_color).rgb_bytes == light_color.rgb_bytes


def test_make_light_dark():
    light_color = Color.from_hls(h=100, l=0.8, s=0.8)
    dark_color  = Color.from_hls(h=100, l=0.2, s=0.8)
    
    assert invert_lightness(light_color).rgb_bytes == dark_color.rgb_bytes
