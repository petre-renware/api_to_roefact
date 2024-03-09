#!../.venv/bin/python3
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

__version__ = "0.3.1b1"





def normalized_version(raw_version: str) -> str:
    """transform version string in canonical form.

    Usage:
    - `import xl2roefact`
    - `xl2roefact.__version__.normalized_version()`

    Args:
        `raw_version (str)`: raw version string

    Returns:
        `str:` canonical version string
    """
    return packaging.utils.canonicalize_version(raw_version)


