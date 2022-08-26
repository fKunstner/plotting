"""
Helper functions for themes and global settings
"""

from fplt.colors import COLORS


def enable_latex(matplotlib, packages=None):
    """
    Enables latex for the given matplotlib instance.

    A list of package names can be passed to be loaded in the preamble.
    Defaults to loading amsmath.
    """
    if packages is None:
        packages = ["amsmath"]

    preamble = [r"\usepackage{%s}" % package for package in packages]

    matplotlib.rcParams["text.usetex"] = True
    matplotlib.rcParams["text.latex.preamble"] = [preamble]


def set_font_size(matplotlib, size=18, family=None):
    """
    Sets the font size (default: 18) and family (default: "serif")
    """
    font = {"size": size}
    if family is not None:
        font["family"] = family
    matplotlib.rc("font", **font)


def load_style(mpl, stylename="anim"):
    styles = {
        "anim": {
            "figure.facecolor": "#F3F3F3",
            "axes.facecolor": "#F3F3F3",
            "axes.prop_cycle": mpl.cycler(color=COLORS["CC"]),
            "image.cmap": "YlOrBr",
        },
        "paper": {
            "axes.prop_cycle": mpl.cycler(color=COLORS["CC"]),
            "image.cmap": "YlOrBr",
        },
    }
    for k, v in styles[stylename].items():
        mpl.rcParams[k] = v
