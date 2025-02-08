from colorzero.color import Color
import re
import sys
from typing import Iterator


def invert_lightness(color: str) -> str:
    """
    Invert a color's lightness. Handle both RGB and RGBA colors.

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

def _find_color_patterns(text: str) -> Iterator[tuple[str, int, int]]:
    """Find CSS color patterns in text and return them with their positions."""
    # Match both 6-digit and 8-digit hex colors
    pattern = r'#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?'
    for match in re.finditer(pattern, text):
        yield (match.group(0), match.start(), match.end())

def invert_colors(filename: str) -> None:
    """
    Read a file, invert all CSS color codes, and print the result to stdout.
    
    Args:
        filename: Path to the file to process
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Process the content from end to start to maintain correct positions
        matches = list(_find_color_patterns(content))
        result = list(content)
        
        for color, start, end in reversed(matches):
            inverted = invert_lightness(color)
            result[start:end] = inverted
            
        sys.stdout.write(''.join(result))
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
    except Exception as e:
        print(f"Error processing file: {str(e)}", file=sys.stderr)
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Invert CSS color codes")
    parser.add_argument("filename", help="Path to the file to process")
    args = parser.parse_args()
    
    invert_colors(args.filename)
