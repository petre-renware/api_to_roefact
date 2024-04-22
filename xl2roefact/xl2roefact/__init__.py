# canonical version converter
from xl2roefact.__version__ import normalized_version

# public symbols to expose
from xl2roefact.rdinv import rdinv  # status #TODO: wip...
from xl2roefact.wrxml import wrxml  # status #FIXME: not yet started
from xl2roefact.chkxml import chkxml  # status #FIXME: not yet started
from xl2roefact.ldxml import ldxml  # status #FIXME: not yet started
from xl2roefact.chkisld import chkisld  # status #FIXME: not yet started
import xl2roefact.sys_settings

__version__ = normalized_version()  # default conversion takes place over xl2roefact actual version

