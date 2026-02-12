Contributing
============

We welcome and encourage contributions to the ChatterBot Corpus! This project relies on community contributions to provide high-quality, diverse training data for chatbots across multiple languages.

For complete contributing guidelines, please see the `CONTRIBUTING.md <https://github.com/gunthercox/chatterbot-corpus/blob/master/CONTRIBUTING.md>`_ file in the repository.

Content Quality Standards
--------------------------

The corpus aims for:

* **Factual correctness** - All factual information should be accurate and verifiable
* **Proper grammar and spelling** - Content must meet high quality standards for the target language  
* **Natural conversation flow** - Conversations should flow naturally and contextually

Legal Requirements
------------------

**Important:** All contributions must be original work or freely licensed content. 

Contributions must **not** include:

* Copyrighted material (dialogue from movies, books, TV shows, etc.)
* Song lyrics or poetry under copyright
* Content that violates intellectual property rights
* Illegal, harmful, or offensive content

Contributions must:

* Be your original work
* Be freely licensed or in the public domain
* Not violate any copyright, trademark, or intellectual property rights
* Be appropriate for public distribution

Quick Start for Contributors
-----------------------------

1. **Fork the repository** on GitHub
2. **Create a new branch** for your contribution
3. **Add or improve** YAML conversation files in ``chatterbot_corpus/data/``
4. **Ensure** proper formatting, grammar, and factual accuracy
5. **Submit a pull request** with a clear description

File Format
-----------

All corpus data files use YAML format (``.yml``). Here's the basic structure:

.. code-block:: yaml

   categories:
   - greetings
   - casual

   conversations:
   - - Hello
     - Hi there!
   - - How are you?
     - I'm doing well, thank you! How about you?
   - - What's your name?
     - I'm a chatbot. What's your name?

Adding New Languages
--------------------

To add support for a new language:

1. Create a new directory under ``chatterbot_corpus/data/`` with the language name
2. Add conversation files in YAML format (``.yml``)
3. Follow the existing structure from other language directories
4. Ensure translations are accurate and culturally appropriate

Improving Existing Content
---------------------------

You can help by:

* Adding new conversation topics to existing languages
* Correcting factual errors in existing conversations
* Fixing spelling, grammar, or formatting issues
* Expanding topic coverage within a language
* Improving the natural flow of conversations

Full Guidelines
---------------

For detailed information including:

* Step-by-step setup instructions
* YAML formatting guidelines
* Pull request process
* Language-specific guidelines
* Style guide and best practices
* Detailed legal requirements

Please refer to `CONTRIBUTING.md <https://github.com/gunthercox/chatterbot-corpus/blob/master/CONTRIBUTING.md>`_ in the repository.

Questions?
----------

If you have questions about contributing:

1. Check existing `issues and pull requests <https://github.com/gunthercox/chatterbot-corpus/issues>`_ on GitHub
2. Review the `CONTRIBUTING.md <https://github.com/gunthercox/chatterbot-corpus/blob/master/CONTRIBUTING.md>`_ guide thoroughly
3. `Open a new issue <https://github.com/gunthercox/chatterbot-corpus/issues/new>`_ with your question if you can't find an answer

Thank you for helping make ChatterBot better for everyone!
