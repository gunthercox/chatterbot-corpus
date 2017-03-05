from unittest import TestCase
from unittest import SkipTest
from chatterbot import ChatBot


class ChatBotTestCase(TestCase):

    def setUp(self):
        self.test_data_directory = None
        self.chatbot = ChatBot('Test Bot', **self.get_kwargs())

    def assertIsLength(self, item, length):
        """
        Assert that an iterable has the given length.
        """
        if len(item) != length:
            raise AssertionError(
                'Length {} is not equal to {}'.format(len(item), length)
            )

    def get_kwargs(self):
        return {
            'input_adapter': 'chatterbot.input.VariableInputTypeAdapter',
            'output_adapter': 'chatterbot.output.OutputAdapter',
            'database': None, # None runs the database in-memory
            'silence_performance_warning': True
        }

    def random_string(self, start=0, end=9000):
        """
        Generate a string based on a random number.
        """
        from random import randint
        return str(randint(start, end))

    def tearDown(self):
        """
        Remove the test database.
        """
        self.chatbot.storage.drop()
