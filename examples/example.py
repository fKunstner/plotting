"""
Showcase
========================================
"""

import matplotlib.pyplot as plt
import numpy as np
import fplt

import warnings

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Matplotlib is currently using agg, which is a"
    " non-GUI backend, so cannot show the figure.",
)
# %%
# Loading some data to plot

np.random.seed(0)
data = {
    "x1": list(range(100)),
    "y1": [np.exp(-t) * (1 + np.random.randn() ** 2) for t in range(100)],
    "x2": list(range(100)),
    "y2": [1 / (t + 1) * (1 + 5 * np.random.randn() ** 2) for t in range(100)],
}

# %%
# Preparing the figure and make a grid

fig = plt.figure(figsize=(8, 3))
ax1, ax2 = fplt.make_grid(fig, nrows=1, ncols=2)

plt.show()

# %%
# Adding the data

fig = plt.figure(figsize=(8, 3))
ax1, ax2 = fplt.make_grid(fig, nrows=1, ncols=2)

(lh1,) = ax1.plot(data["x1"], data["y1"])
(lh2,) = ax2.plot(data["x2"], data["y2"])

plt.show()

# %%
# Adding some color and line style

fig = plt.figure(figsize=(8, 3))
ax1, ax2 = fplt.make_grid(fig, nrows=1, ncols=2)

style = {"linestyle": "-", "linewidth": 2}
blue = fplt.COLORS["PT"]["VB"]["blue"]
red = fplt.COLORS["PT"]["VB"]["red"]

(lh1,) = ax1.plot(data["x1"], data["y1"], color=red, **style)
(lh2,) = ax2.plot(data["x2"], data["y2"], color=blue, **style)

plt.show()

# %%
# Removing the frame

fig = plt.figure(figsize=(8, 3))
ax1, ax2 = fplt.make_grid(fig, nrows=1, ncols=2)

style = {"linestyle": "-", "linewidth": 2}

(lh1,) = ax1.plot(data["x1"], data["y1"], color=red, **style)
(lh2,) = ax2.plot(data["x2"], data["y2"], color=blue, **style)

fplt.hide_frame(ax1, ax2, left=False, bottom=False, top=True, right=True)

plt.show()

# %%
# Normalizing the y limits

fig = plt.figure(figsize=(8, 3))
ax1, ax2 = fplt.make_grid(fig, nrows=1, ncols=2)

style = {"linestyle": "-", "linewidth": 2}

(lh1,) = ax1.plot(data["x1"], data["y1"], color=red, **style)
(lh2,) = ax2.plot(data["x2"], data["y2"], color=blue, **style)

fplt.hide_frame(ax1, ax2, left=False, bottom=False, top=True, right=True)
fplt.normalize_y_axis(ax1, ax2)

plt.show()

# %%
# On the same plot in log scale

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(1, 1, 1)

style = {"linestyle": "-", "linewidth": 2}

(lh1,) = ax.plot(data["x1"], data["y1"], color=red, **style, label="Linear")
(lh2,) = ax.plot(data["x2"], data["y2"], color=blue, **style, label="Sublinear")

fplt.hide_frame(ax, left=False, bottom=False, top=True, right=True)
ax.set_yscale("log")

fplt.labelLine(lh1, x=70, align=False, manual_rotation=-40)
fplt.labelLine(lh2, x=70, align=False, manual_rotation=0)

plt.show()
