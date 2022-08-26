from matplotlib.dates import date2num
from datetime import datetime
from math import atan2, degrees
import warnings
import numpy as np


def labelLine(
    line,
    x,
    label=None,
    align=True,
    drop_label=False,
    manual_rotation=0,
    ydiff=0.0,
    **kwargs,
):
    """Label a single matplotlib line at position x

    Source:
    https://github.com/cphyc/matplotlib-label-lines
    https://stackoverflow.com/questions/16992038/inline-labels-in-matplotlib

    Parameters
    ----------
    line : matplotlib.lines.Line
       The line holding the label
    x : number
       The location in data unit of the label
    label : string, optional
       The label to set. This is inferred from the line by default
    drop_label : bool, optional
       If True, the label is consumed by the function so that subsequent calls to e.g. legend
       do not use it anymore.
    kwargs : dict, optional
       Optional arguments passed to ax.text
    """
    ax = line.axes
    xdata = line.get_xdata()
    ydata = line.get_ydata()

    mask = np.isfinite(ydata)
    if mask.sum() == 0:
        raise Exception("The line %s only contains nan!" % line)

    # Find first segment of xdata containing x
    if len(xdata) == 2:
        i = 0
        xa = min(xdata)
        xb = max(xdata)
    else:
        for i, (xa, xb) in enumerate(zip(xdata[:-1], xdata[1:])):
            if min(xa, xb) <= x <= max(xa, xb):
                break
        else:
            raise Exception("x label location is outside data range!")

    def x_to_float(x):
        """Make sure datetime values are properly converted to floats."""
        return date2num(x) if isinstance(x, datetime) else x

    xfa = x_to_float(xa)
    xfb = x_to_float(xb)
    ya = ydata[i]
    yb = ydata[i + 1]
    y = ya + (yb - ya) * (x_to_float(x) - xfa) / (xfb - xfa)

    if not (np.isfinite(ya) and np.isfinite(yb)):
        warnings.warn(
            (
                "%s could not be annotated due to `nans` values. "
                "Consider using another location via the `x` argument."
            )
            % line,
            UserWarning,
        )
        return

    if not label:
        label = line.get_label()

    if drop_label:
        line.set_label(None)

    if align:
        # Compute the slope and label rotation
        screen_dx, screen_dy = ax.transData.transform(
            (xfa, ya)
        ) - ax.transData.transform((xfb, yb))
        rotation = (degrees(atan2(screen_dy, screen_dx)) + 90) % 180 - 90
    else:
        rotation = manual_rotation

    # Set a bunch of keyword arguments
    if "color" not in kwargs:
        kwargs["color"] = line.get_color()

    if ("horizontalalignment" not in kwargs) and ("ha" not in kwargs):
        kwargs["ha"] = "center"

    if ("verticalalignment" not in kwargs) and ("va" not in kwargs):
        kwargs["va"] = "center"

    if "backgroundcolor" not in kwargs:
        kwargs["backgroundcolor"] = ax.get_facecolor()

    if "clip_on" not in kwargs:
        kwargs["clip_on"] = True

    if "zorder" not in kwargs:
        kwargs["zorder"] = 2.5

    ax.text(x, y + ydiff, label, rotation=rotation, **kwargs)
