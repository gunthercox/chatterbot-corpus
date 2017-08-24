Data Format
===========

The data file contained in ChatterBot Corpus is formatted using `YAML`_ syntax.
This format is used because it is easily readable by both humans and machines.

.. list-table:: Corpus Properties
   :widths: 15 10 30
   :header-rows: 1

   * - Property
     - Required
     - Description
   * - categories
     - Required
     - A list of categories that describe the conversations.
   * - conversations
     - Optional
     - A list of conversations. Each conversation is denoted as a list.

Here is an example of the corpus data:

.. code-block:: yaml
   :name: corpus-example.yml

   categories:
   - english
   - greetings
   conversations:
   - - Hello
     - Hi
   - - Hello
     - Hi, how are you?
     - I am doing well.
   - - Good day to you sir!
     - Why thank you.
   - - Hi, How is it going?
     - It's going good, your self?
     - Mighty fine, thank you.

The values in this example have the following relationships.

.. list-table:: Evaluated statement relationships
   :widths: 15 40
   :header-rows: 1

   * - Statement
     - Response
   * - Hello
     - Hi
   * - Hello
     - Hi, how are you?
   * - Hi, how are you?
     - I am doing well.
   * - Good day to you sir!
     - Why thank you.
   * - Hi, How is it going?
     - It's going good, your self?
   * - It's going good, your self?
     - Mighty fine, thank you.

.. _YAML: http://www.yaml.org/
