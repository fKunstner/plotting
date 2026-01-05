def save(fig, path, tight=True, transparent=False):
    fig.savefig(path, bbox_inches="tight" if tight else None, transparent=transparent)


def save_current(plt, path, transparent=False):
    plt.gcf().savefig(path, transparent=transparent)
