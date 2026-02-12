Installation
============

Requirements
------------

- Python 3.9 or newer
- `PyYAML <https://pyyaml.org/>`_ (installed automatically as a dependency)

Install from PyPI
-----------------

The recommended way to install ``chatterbot-corpus`` is via pip:

.. code-block:: bash

   pip install chatterbot-corpus

Install from Source
-------------------

You can also install from source by cloning the repository:

.. code-block:: bash

   git clone https://github.com/gunthercox/chatterbot-corpus.git
   cd chatterbot-corpus
   pip install .

.. note::

   The ``chatterbot-corpus`` package is a **data-only** package. It contains
   multilingual conversation data in YAML format and a reference to the data
   directory. The functions for loading and parsing this data (such as
   ``load_corpus`` and ``read_corpus``) are provided by the
   `ChatterBot <https://github.com/gunthercox/ChatterBot>`_ library itself.

   To use this corpus for training a chat bot, you will also need to install
   ``chatterbot``:

   .. code-block:: bash

      pip install chatterbot
