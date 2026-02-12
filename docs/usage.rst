Usage
=====

How This Package Relates to ChatterBot
---------------------------------------

The ``chatterbot-corpus`` package provides the **data** — multilingual
conversation files in YAML format. The ``chatterbot`` package provides the
**loading and training functions** that read this data and use it to train
a chat bot.

When you install ``chatterbot-corpus``, it makes a ``DATA_DIRECTORY`` path
available that points to the bundled YAML files. ChatterBot's training
utilities use this path to locate and load the corpus data.

Training a Chat Bot
-------------------

To train a ChatterBot instance using the corpus data, use ChatterBot's
``ChatterBotCorpusTrainer``:

.. code-block:: python

   from chatterbot import ChatBot
   from chatterbot.trainers import ChatterBotCorpusTrainer

   # Create a new chat bot
   chatbot = ChatBot('My ChatBot')

   # Create a trainer
   trainer = ChatterBotCorpusTrainer(chatbot)

   # Train using all English corpus data
   trainer.train('chatterbot.corpus.english')

Training with Specific Topics
-----------------------------

You can train on a specific topic within a language by appending the
topic name:

.. code-block:: python

   # Train only on English greetings
   trainer.train('chatterbot.corpus.english.greetings')

   # Train only on English humor
   trainer.train('chatterbot.corpus.english.humor')

Training with Multiple Languages
---------------------------------

You can train on multiple languages by calling ``train()`` multiple times:

.. code-block:: python

   trainer.train('chatterbot.corpus.english')
   trainer.train('chatterbot.corpus.spanish')
   trainer.train('chatterbot.corpus.french')

Accessing the Data Directory
-----------------------------

If you need to access the raw YAML files programmatically, you can use the
``DATA_DIRECTORY`` constant:

.. code-block:: python

   from chatterbot_corpus.corpus import DATA_DIRECTORY
   import os

   # List all available language directories
   languages = os.listdir(DATA_DIRECTORY)
   print(languages)

   # Build a path to a specific corpus file
   greetings_path = os.path.join(DATA_DIRECTORY, 'english', 'greetings.yml')

For more details, see the `ChatterBot Documentation <https://docs.chatterbot.us/corpus/>`_.
