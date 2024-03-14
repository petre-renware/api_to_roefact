# public symbols


#from xl2roefact.__version__ import __version__
from xl2roefact.__version__ import normalized_version

# public symbols to expose
from xl2roefact.rdinv import rdinv  # status #TODO: wip...
from xl2roefact.wrxml import wrxml  # status #FIXME: not yet started
from xl2roefact.chkxml import chkxml  # status #FIXME: not yet started
from xl2roefact.ldxml import ldxml  # status #FIXME: not yet started
from xl2roefact.chkisld import chkisld  # status #FIXME: not yet started

__version__ = normalized_version()

