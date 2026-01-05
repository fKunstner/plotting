"""Helpers and color definitions"""
import numpy as np


def cmap_to_list(cmap, max_colors=256):
    """Converts a colormap to list of colors"""
    clrs = np.unique(cmap(np.linspace(0, 1, max_colors)), axis=0)
    return [list(clrs[i, :]) for i in range(clrs.shape[0])]


def rgb_to_unit(xs):
    """Convert a list of RGB numbers [0, 255] to a list of unit [0, 1]"""
    return [x / 255.0 for x in xs]


def grayscale(index, total):
    """
    RGB value for a grayscale value of `total` colors, index is 1-based.

    Example:
        grayscale(1, 3) = black
        grayscale(2, 3) = dark
        grayscale(3, 3) = light
    """
    inten = (index - 1) / total
    return [inten, inten, inten]


COLORS = {
    "PT": {
        "HC": {
            "white": rgb_to_unit([255, 255, 255]),
            "yellow": rgb_to_unit([221, 170, 51]),
            "red": rgb_to_unit([187, 85, 102]),
            "blue": rgb_to_unit([0, 68, 136]),
            "black": rgb_to_unit([0, 0, 0]),
        },
        "VB": {
            "blue": rgb_to_unit([0, 119, 187]),
            "red": rgb_to_unit([204, 51, 17]),
            "orange": rgb_to_unit([238, 119, 51]),
            "cyan": rgb_to_unit([51, 187, 238]),
            "teal": rgb_to_unit([0, 153, 136]),
            "magenta": rgb_to_unit([238, 51, 119]),
            "grey": rgb_to_unit([187, 187, 187]),
        },
        "BR": {
            "blue": rgb_to_unit([68, 119, 170]),
            "cyan": rgb_to_unit([102, 204, 238]),
            "green": rgb_to_unit([34, 136, 51]),
            "yellow": rgb_to_unit([204, 187, 68]),
            "red": rgb_to_unit([238, 102, 119]),
            "purple": rgb_to_unit([170, 51, 119]),
            "gray": rgb_to_unit([187, 187, 187]),
        },
    }
}
"""
Color values for some color palettes 

``COLORS[source][palette][color name]``

Current sources: PT
Paul Tol's color notes https://personal.sron.nl/~pault/
"""

# COLORS["CC"] = [
#     COLORS["PT"]["VB"]["blue"],
#     COLORS["PT"]["VB"]["red"],
#     COLORS["PT"]["HC"]["yellow"],
#     COLORS["PT"]["VB"]["cyan"],
#     COLORS["PT"]["VB"]["orange"],
#     COLORS["PT"]["VB"]["magenta"],
# ]
