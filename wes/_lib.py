from matplotlib import rcParams
import matplotlib.pyplot as plt
import cycler
import json
import os

pth = os.path.dirname(os.path.realpath(__file__))
datapath = os.path.join(pth, 'colors.json')

_cycles = json.load(open(datapath))


def set_palette(cname):
    """
    set default colormap to a wes anderson palette

    Arguments
    ---------
    cname   :   str
                Name of a palette shown in wes.available()
    """
    try:
        _set_colors(_cycles[cname])
    except KeyError:
        raise KeyError("{cname} is not a recognized palette name. Check wes.avalable() again")

def _set_colors(ccycle):
    """
    set default colormap to any palette

    Arguments
    ----------
    ccycle  :   List
                A list of color indicators matplotlib can understand
    """
    rcParams['axes.prop_cycle'] = cycler.cycler(color=ccycle)

def available(show=True):
    """
    show all available color palettes 

    Arguments
    ----------
    show    :   Bool
                Whether or not to show the palettes as matplotlib plots
    """
    if not show:
        return maps.keys()
    else:
        fig, axes = plt.subplots(8,2, figsize=(6,12))
        fig.tight_layout()
        for i, name in enumerate(_cycles.keys()):
            row = i // 2
            col = i % 2
            cycle = _cycles[name]
            for j,c in enumerate(cycle):
                axes[row,col].hlines(j, 0,1, colors=c,linewidth=30)
            axes[row,col].set_title(name)
            axes[row,col].get_xaxis().set_visible(False)
            axes[row,col].get_yaxis().set_visible(False)
        plt.show()

def plot_palettes(*args):
    """
    Plot any number of color palettes

    Arguments
    ----------
    arg0, arg1, ..., argN   :   str
                                name of palette to plot
    """
    if len(args) > 1:
        fig, axes = plt.subplots(1, len(args))
        for i, name in enumerate(args):
            cycle = _cycles[name]
            for j,c in enumerate(cycle):
                axes[i].hlines(j,0,1,colors=c,linewidth=30)
            axes[i].set_title(name)
            axes[i].get_xaxis().set_visible(False)
            axes[i].get_yaxis().set_visible(False)
        fig.tight_layout()
        plt.show()
    elif len(args) == 1:
        fig = plt.figure()
        cycle = _cycles[args[0]]
        for j,c in enumerate(cycle):
            plt.hlines(j, 0, 1, colors=c, linewidth=30)
        plt.title(args[0])
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('')
        plt.ylabel('')
        plt.show()
    else:
        raise NotImplementedError("No support for your indecision. Pick a palette!!")



        

