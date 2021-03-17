
from matplotlib.colors import LinearSegmentedColormap

_NEMBROTHA = [(0,(0.329,1.0,0.808)), (.25,(0.11,0.506,0.247)), (.5,(0,0,0)), (.75, (0.529,0.039,0.031)), (1.0, (0.969,0.176,0.02))]
_FLABELLINA = [(0,(0.953,0.318,0.137)), (0.25,(0.992,0.855,0.4)), (.5,(0.937,0.522,0.714)), (.75, (0.408,0.106,0.624)), (1.0, (0.337,0.396,1))]
_BERGHIA = [(0,(0.992,0.996,0.005)), (0.25,(1.,0.659,0.035)), (.5,(0.922,0.725,0.392)), (0.75, (0.239,0.722,0.988)), (1.0,(0.098,0.31,0.553))]
_FELIMARE = [(0,(0.996,0.824,0.004)), (0.5,(0,0.098,0.376)), (1.,(0.008,0.455,0.843))]
_GLAUCUS = [(0,(0.004,0.086,0.435)), (0.5,(0.447,0.647,0.957)), (1.0,(0.918,0.953,0.973))]
_AUREA = [(0., (0.443,0.004,0.0)), (0.2, (0.996,0.322,0.024)), (.4,(0.788,0.788,0.890)), (.5,(0.71,0.745,0.435)),  (.6, (0.431,0.392,0.906)), (0.8, (0.42,0.0,0.639)), (1.,(0.796,0.0,0.694))]
_CERATOSOMA = [(0., (0.451,0.051,0.094)), (0.33, (0.761,0.498,0.80)), (.67,(0.827,0.91,0.91)), (1,(0.976,0.455,0.161))]
_GONIOBRACHUS = [(0., (0.525,0.0,0.106)), (0.2, (0.659,0.306,0.588)), (.4, (0.055,0.373,1.0)), (.6,(0.867,0.918,0.851)),  (.8,(0.988,0.831,0.008)), (1., (0.871,0.196,0.0))]

cmaps = ['nembrotha', 'flabellina', 'berghia', 'felimare', 'glaucus', 'aurea', 'ceratosoma', 'goniobrachus']

def get_cmap(name, N=None):
    if name.endswith('_r'):
        reverse = True
        name = name[:-2]
    else:
        reverse = False

    if name not in cmaps:
        s = '\'{:s}\' is not a valid value for name; supported values are '.format(name)
        for cmap in cmaps:
            s += '\'{:s}\', \'{:s}_r\','.format(cmap, cmap)
        raise ValueError(s[:-1])

    colors = globals()['_'+name.upper()]
    if reverse:
        colors = list(zip([c for c,_ in colors],[c for _,c in colors][::-1]))

    return LinearSegmentedColormap.from_list(name, colors)

locals().update(dict([(cmap, get_cmap(cmap)) for cmap in cmaps]+[(cmap+'_r', get_cmap(cmap+'_r')) for cmap in cmaps]))

