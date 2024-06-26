"""`xl2roefact` version info.
```
######## ####              ########  ######
#  ##  # #  #              #      # ##    ##
##    ## #  #              ###  ### #  ##  #
##  ##  #  #                #  #   #  ##  #
##    ## #  #                #  #   #  ##  #
#  ##  # #  #####            #  #   #  ##  #
#  ##  # #      #            #  #   ##    ##
######## ########            ####    ######

                           ######## ########  ######   ######  ########
#######   ######           #      # #     #  ##    ## ##    ## #      #
#     ## ##    ## #######  #  ##### #  ####  #  ##  # #  ##  # ###  ###
#  ##  # #  ##  # #     #  #    #   #    #   #      # #  #####   #  #
#  ##### #  ##  # #######  #  ###   #  ###   #  ##  # #  #####   #  #
#  # #   #  ##  #          #  ##### #  #     #  ##  # #  ##  #   #  #
#  #  #  ##    ##          #      # #  #     #  ##  # ##    ##   #  #
####   #  ######           ######## ####     ########  ######    ####
```
"""

import packaging.utils

__version__ = "0.8"  # current 0.8, previous 0.7


def normalized_version(
    raw_version: str = __version__
) -> str:
    """transform version string in canonical form.

    Used in `__init__.py` to return `__version__` object as will be seen by package consumers

    Args:
    
        `raw_version`: a raw version string. Defaults to package current version string.

    Returns:
    
        `str:` canonical version string
    """
    return packaging.utils.canonicalize_version(raw_version)


