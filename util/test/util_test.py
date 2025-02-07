import pytest

from colorzero.color import Color
from util import invert_lightness


def test_invert_lightness():
    color = Color(255, 0, 0)
    inverted_color = invert_lightness(color)
    assert inverted_color == Color(0, 255, 255)
