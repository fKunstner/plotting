"""
Manipulating multiple axes, labels and ticks
"""
import numpy as np


def hide_frame(*axes, top=True, right=True, left=False, bottom=False):
    """Hides the frame/spine of the axes"""
    for ax in axes:
        ax.spines["top"].set_visible(not top)
        ax.spines["right"].set_visible(not right)
        ax.spines["left"].set_visible(not left)
        ax.spines["bottom"].set_visible(not bottom)


def hide_all_frame(*axes):
    """See `hide_frame`"""
    hide_frame(*axes, top=True, right=True, left=True, bottom=True)


def hide_labels(*axes, x=True, y=True):
    """Hide labels on specified axis"""
    for ax in axes:
        if x:
            ax.set_xlabel("")
        if y:
            ax.set_ylabel("")


def hide_ticklabels(*axes, x=True, y=True):
    """Removes the ticklabels for the specified axis"""
    for ax in axes:
        if x:
            ax.set_xticklabels([], minor=True)
            ax.set_xticklabels([], minor=False)
        if y:
            ax.set_yticklabels([], minor=True)
            ax.set_yticklabels([], minor=False)


def hide_ticks(*axes, x=True, y=True):
    """Removes the ticklabels for the specified axis"""
    for ax in axes:
        if x:
            ax.set_xticks([], minor=True)
            ax.set_xticks([], minor=False)
        if y:
            ax.set_yticks([], minor=True)
            ax.set_yticks([], minor=False)


def clean_ax(*axes):
    """Hide ticks and ticklabels on all axis"""
    for ax in axes:
        hide_ticklabels(ax)
        hide_ticks(ax)


def strip_axes(axes):
    """Hide ticks and labels on all axis"""
    hide_ticks(axes)
    hide_labels(axes)


def equalize_xy_axes(*axes):
    """Equalize the x and y limits to be the same

    Ensures that ``ax.get_xlim() == ax.get_ylim()`` for each ``ax``
    """
    for ax in axes:
        axlimits = [*ax.get_xlim(), *ax.get_ylim()]
        minlim, maxlim = np.min(axlimits), np.max(axlimits)
        ax.set_xlim([minlim, maxlim])
        ax.set_ylim([minlim, maxlim])


def normalize_y_axis(*axes):
    """Sets the y limits to be the same for all the axes

    Ensures that ``ax1.get_ylim() == ax2.get_ylim()`` for all ``ax1, ax2``
    """
    miny, maxy = np.inf, -np.inf
    for ax in axes:
        y1, y2 = ax.get_ylim()
        miny = np.min([miny, y1])
        maxy = np.max([maxy, y2])
    for ax in axes:
        ax.set_ylim([miny, maxy])
