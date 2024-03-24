
"""xl2roefact version info.
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

__version__ = "0.4.1.dev1"





def normalized_version(
    raw_version: str = __version__
) -> str:
    """transform version string in canonical form.

    Usage:
    - `import xl2roefact`
    - `xl2roefact.__version__.normalized_version()`

    Args:
        `raw_version (str)`: a raw version string. Defaults to package current version string.

    Returns:
        `str:` canonical version string
    """
    return packaging.utils.canonicalize_version(raw_version)


