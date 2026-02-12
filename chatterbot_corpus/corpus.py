"""
Corpus data path constants.

This module provides the file system paths used to locate
the bundled YAML conversation data files.
"""

import os


#: Absolute path to the directory containing this module.
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

#: Absolute path to the ``data/`` directory that contains
#: all of the YAML corpus files, organized by language.
DATA_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'data')
