# ChatterBot Language Training Corpus

[![Package Version](https://img.shields.io/pypi/v/chatterbot-corpus.svg)](https://pypi.python.org/pypi/chatterbot-corpus/)
[![Build Status](https://travis-ci.org/gunthercox/chatterbot-corpus.svg?branch=master)](https://travis-ci.org/gunthercox/chatterbot-corpus)

These modules are used to quickly train ChatterBot to respond to various inputs in different languages.
Although much of ChatterBot is designed to be language independent, it is still useful to have these
training sets available to prime a fresh database and make the variety of responses that a bot can yield
much more diverse.

For instructions on how to use these data sets, please refer to the [project documentation](http://chatterbot.readthedocs.io/en/latest/training.html#training-with-corpus-data).

All training data contained within this corpus is user contributed.

If you are interested in contributing support for a new language please create a pull request. Additions are welcomed!

# Create your own Corpus Training data

Chatterbot is a very flexible and dynamic chatbot that you easily can create your own training data and structure.

Create or copy an existing .yml file and put that file in a existing or a new directory you created under `chatterbot_corpus\data\<NEW DIRECTORY>`
Edit that file with any text editor that you like to work with.

In the beginning of the file you set one or two categories.
```
categories:
- myown
- my own categories
````

Then can you start your actual training conversation data.

```
conversations:
- - Hello
  - Hello
- - Hi
  - Hello
```

# Install your training corpus data to Django
You need to install chatterbot as the [Quick Start Guide](http://chatterbot.readthedocs.io/en/stable/quickstart.html).
When the installation are done, please go to `(Virtual Env)/lib/pythonX.X/site-packages/chatterbot_corpus/data/` directory.
Here is the same structure as you can find in this GitHub repo, here is the area where you can create your own directories and conversation files.

When you are done with your files, then can you edit the Django `setting.py` file and locate the chatterbot training section. 
Here do you need to add `chatterbot.corpus.<DIRECTORY>.<FILENAME>`

```
    'training_data': [
         'chatterbot.corpus.english.greeting',
         'chatterbot.corpus.custom.myown',
         'chatterbot.corpus.swedish.food'
    ]
```

When you are done, please proceed with the Django Chatterbot Training session. 

# Unit Testing

“A true professional does not waste the time and money of other people by handing over software that is not reasonably free of obvious bugs; that has not undergone minimal unit testing; that does not meet the specifications and requirements; that is gold-plated with unnecessary features; or that looks like junk.” – Daniel Read

```
pip install -r dev-requirements.txt
nosetests
```
