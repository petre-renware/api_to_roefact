# canonical version converter
from .__version__ import normalized_version

# basic components, public symbols to expose
from .rdinv import rdinv  # status RDY (@2024.april [piu] tested. PASS)
from .wrxml import wrxml  # status #FIXME: not yet started
from .chkxml import chkxml  # status #FIXME: not yet started
from .ldxml import ldxml  # status #FIXME: not yet started
from .chkisld import chkisld  # status #FIXME: not yet started

# command components, public symbols to expose
from .commands import Commands

# general info exposed
__version__ = normalized_version()  # default conversion takes place over xl2roefact actual version

