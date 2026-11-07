
__version__ = '3.2.7'
__message__ = ('Version 3.2 is now online with new features, including connection with GAIA DR3!'
               '\nv3.2.1 - Avoid bright stars in alignment, version control for reduction.'
               '\nv3.2.2 - Fix GAIA catalogue bug.'
               '\nv3.2.3 - Fix installation overwriting older versions.'
               '\nv3.2.4 - Matplotlib==3.9.0 bug fixed.'
               '\nv3.2.5 - Updated installation process'
               '\nv3.2.6 - Handling of saturated stars and better gary scale for plots.'
               '\nv3.2.7 - Sync with v4.0 and add long-term-support:'
               '\n       - Filter out frames with saturated pixels in Photometry.'
               '\n       - Bypass exotethys loading error when paths have spaces.'
               '\n       - Fix alignment bug for small number of stars.'
               '\n       - Correct bad pixels in flat frames, improvements in alignment and plate-solving.'
               '\n       - Check for alternative Simbad connections.'
               )

from .__run__ import run_app


def __get_abspath__():
    import os
    return os.path.abspath(os.path.dirname(__file__))
