# ChatterBot Language Training Corpus

[![Package Version](https://img.shields.io/pypi/v/chatterbot-corpus.svg)](https://pypi.python.org/pypi/chatterbot-corpus/)

These modules are used to quickly train ChatterBot to respond to various inputs in different languages.
Although much of ChatterBot is designed to be language independent, it is still useful to have these
training sets available to prime a fresh database and make the variety of responses that a bot can yield
much more diverse.

All training data contained within this corpus is user contributed.

## Documentation

Documentation is available at:
http://corpus.chatterbot.us/

## Content Quality

We strive for factual correctness, proper grammar, and spelling in all corpus content. However, as this is a community-contributed project, there may be occasional mistakes or inaccuracies. If you find any errors or would like to contribute improvements, please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to help.

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

# Unit Testing

> “A true professional does not waste the time and money of other people by handing over software that is not reasonably free of obvious bugs; that has not undergone minimal unit testing; that does not meet the specifications and requirements; that is gold-plated with unnecessary features; or that looks like junk.”
> 
> – Daniel Read

```bash
python -Wonce -m unittest discover -s tests -v
```
