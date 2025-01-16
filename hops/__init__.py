
__version__ = '3.2.6'
__message__ = 'Version 3.2 is now online with new features, including connection with GAIA DR3!\nv3.2.1 - Avoid bright stars in alignment, version control for reduction.\nv3.2.2 - Fix GAIA catalogue bug.\nv3.2.3 - Fix installation overwriting older versions.\nv3.2.4 - Matplotlib==3.9.0 bug fixed.\nv3.2.5 - Updated installation process\nv3.2.6 - Handling of saturated stars and better gary scale for plots.'

from .__run__ import run_app


def __get_abspath__():
    import os
    return os.path.abspath(os.path.dirname(__file__))
