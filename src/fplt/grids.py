"""Making grid and axes
"""

import matplotlib as mpl

from fplt.axes import hide_ticks, hide_ticklabels, hide_all_frame


def make_grid(fig, nrows=1, ncols=1, **kwargs):
    """Creates a grid on fig and returns a list (or list of lists) of axes

    kwargs are passed to ``add_gridspec``
    """
    gs = fig.add_gridspec(nrows=nrows, ncols=ncols, **kwargs)
    if nrows == 1 or ncols == 1:
        axes = []
        for i in range(nrows):
            for j in range(ncols):
                axes.append(fig.add_subplot(gs[i, j]))
    else:
        axes = []
        for i in range(nrows):
            axes.append([])
            for j in range(ncols):
                axes[i].append(fig.add_subplot(gs[i, j]))
    return axes


def make_figure_list(n, scaling=4, marg=0.1):
    """Makes a list of n square axes (n columns)"""
    fig = mpl.pyplot.figure(figsize=(n * scaling, scaling))
    h_marg = marg
    W = (1.0 - (n + 1) * h_marg) / n
    H = n * W
    v_marg = (1.0 - H) / 2
    axes = [fig.add_axes([(i + 1) * h_marg + i * W, v_marg, W, H]) for i in range(n)]
    return fig, axes


def make_full_axis(fig):
    """Makes an axes that takes the whole figure"""
    gs = fig.add_gridspec(nrows=1, ncols=1, left=0.0, right=1.0, top=1.0, bottom=0.0)
    ax = fig.add_subplot(gs[0, 0])
    hide_ticks(ax)
    hide_ticklabels(ax)
    hide_all_frame(ax)
    return ax
