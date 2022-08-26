"""
Basic helpers to plot shapes
"""

import numpy as np


def circle_points(x, y, r, density=100):
    """Cartesian coordinates for a circle of radius r centered at (x, y)."""
    thetas = np.linspace(0, 2 * np.pi, density)
    xs = x + r * np.cos(thetas)
    ys = y + r * np.sin(thetas)
    return xs, ys


def ellipse_points(center, A, scaling=1.0, density=100):
    """Returns the cartesian coordinates of an ellipse centered at center
    with shape given by the matrix A.

    Corresponds to the level ``f(x) = 1`` for ``f(x) = (x-c)^T A (x-c)``.
    """
    CIRCLEGRID = np.linspace(0, 2 * np.pi, density)
    A = np.linalg.inv(A) * scaling
    xs = A[0, 0] * np.sin(CIRCLEGRID) + A[0, 1] * np.cos(CIRCLEGRID) + center[0]
    ys = A[1, 1] * np.cos(CIRCLEGRID) + A[1, 0] * np.sin(CIRCLEGRID) + center[1]
    return xs, ys


def plot_circle(ax, x, y, r, density=100, **kwargs):
    """
    Plots a circle of radius r on ax, centered at (x, y).
    Additional key-value arguments are passed to ax.plot
    """
    thetas = np.linspace(0, 2 * np.pi, density)
    xs = x + r * np.cos(thetas)
    ys = y + r * np.sin(thetas)
    ax.plot(xs, ys, **kwargs)


def axis(ax, x=True, y=True, color="k", alpha=0.2):
    """Draws an axis at x=0 and/or y=0"""
    if x:
        ax.axhline(0, color=color, alpha=alpha)
    if y:
        ax.axvline(0, color=color, alpha=alpha)
