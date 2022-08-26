def save(fig, name, tight=True, transparent=False):
    """Save figure under given filename"""
    fig.savefig(name, bbox_inches="tight" if tight else None, transparent=transparent)


def save_current(plt, name, transparent=False):
    """Save current figure under given filename"""
    plt.gcf().savefig(name, transparent=transparent)
