# nudibranch

An utterly unnecessary custom colormap library inspired by the psychedelic sea slugs.

## installation

```bash
pip install nudibranch
```

## use

```bash
from nudibranch import cm

from nudibranch.colormaps import berghia

aurea_r = cm.get_cmap('aurea_r')

ax.imshow(z, cmap=aurea_r)

ax.imshow(z, cmap=berghia)
```
etc

## Author

David Dempsey (Civil and Natural Resource Engineering, University of Canterbury)