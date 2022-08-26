"""
Misc helper functions
"""

import numpy as np


def percentage_to_index(p, L):
    """For a list of length L, returns the index closest to percentage p"""
    return int(p * (L - 1))


def dummy(*args, **kwargs):
    """No-op"""
    return None


def nice_logspace(start, stop, density, base=10):
    """Returns a log-spaced grid between base**start and base**end

    Increasing the density will repeat previously hit values

    Plays nicely with ``merge_grids`` to merge a sparse and a dense grid
    ``merge_grids(nice_logspace(-4, 3, density=1), nice_logspace(-2, 0, density=2)``

    Start, end and density are assumed to be integers
    Density = 1 will return (end - start) points
    Increasing density by 1 doubles the number of points
    """
    if density < 1 or not np.allclose(int(density), density):
        raise ValueError(f"Density needs to be an integer >= 1, got {density}.")
    if not np.allclose(int(start), start) or not np.allclose(int(stop), stop):
        raise ValueError(f"Start and end need to be integers, got {start, stop}.")
    if not (stop > start):
        raise ValueError(f"Start needs to be smaller than stop, got {start, stop}.")
    assert stop > start
    return np.logspace(
        start, stop, base=base, num=(stop - start) * (2 ** (density - 1)) + 1
    )


def merge_grids(*grids):
    """Merge two lists as sets

    Given lists [a,b,c], [c,d,e], returns [a,b,c,d,e]
    """
    return sorted(list(set.union(*[set(grid) for grid in grids])))


def fullscreen(plt):
    """Makes a plot full screen"""
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()


def get_aspectratio(fig):
    """Returns the aspect ratio of a figure"""
    s = fig.get_size_inches()
    return s[0] / s[1]


def extend_range(limits, multiplier=2.0):
    """Extends a range [a, b] to widen the gap ``|a-b|`` by ``multiplier``

    Useful for zooming out of specific region
    """
    mid = (limits[1] - limits[0]) / 2
    width = limits[1] - limits[0]
    newlimits = [mid - (multiplier / 2.0) * width, mid + (multiplier / 2.0) * width]
    return newlimits


def make_linear_curve_in_logspace(ax):
    xlims = ax.get_xlim()
    from_b10_x, to_b10_x = [
        np.ceil(np.log10(xlims[0])),
        np.floor(np.log10(xlims[1])),
    ]
    x_b10_powers = np.linspace(from_b10_x, to_b10_x, int(to_b10_x - from_b10_x) + 1)

    ylims = ax.get_ylim()
    from_b10_y, to_b10_y = [
        np.ceil(np.log10(ylims[0])),
        np.floor(np.log10(ylims[1])),
    ]
    y_b10_powers = np.linspace(
        from_b10_y,
        to_b10_y + to_b10_x - from_b10_x,
        int(to_b10_y - from_b10_y + to_b10_x - from_b10_x) + 1,
    )

    for x in x_b10_powers:
        ax.axvline(10 ** x, alpha=0.5, color="gray", linestyle="--")
    for y in y_b10_powers:
        ax.axline(
            [10 ** from_b10_x, 10 ** y],
            [10 ** to_b10_x, 10 ** (y - (to_b10_x))],
            alpha=0.5,
            color="gray",
            linestyle="--",
        )


def set_alpha(ax, alpha):
    """
    Sets an alpha value to an Axes, spine and ticks
    """
    ax.patch.set_alpha(alpha)
    for line in ax.lines:
        line.set_alpha(alpha)
    for spine in ax.spines.values():
        spine.set_alpha(alpha)
    ax.tick_params("both", colors=(0, 0, 0, alpha))
