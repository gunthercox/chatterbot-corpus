import os
import sys
import inspect
from unittest import TestCase
from chatterbot import corpus
from chatterbot import languages
from chatterbot_corpus.corpus import DATA_DIRECTORY


'''
This is a somewhat arbitrary limit on the number of characters
that can be in a single statement. We check the length of each
statement in the corpus to keep the lengths of text within the
corpus consistent.

This value can be increased in rare cases when needed.
'''
STATEMENT_TEXT_MAX_LENGTH = 1100


class CorpusUtilsTestCase(TestCase):
    """
    This test case is designed to make sure that all
    corpus data adheres to a few general rules.
    """

    def test_character_count(self):
        """
        Test that no line in the corpus exceeds the maximum number of characters.
        """
        files = corpus.list_corpus_files('chatterbot_corpus')

        for dialog_corpus, _categories, _file_path in corpus.load_corpus(*files):
            for conversation in dialog_corpus:
                for text in conversation:
                    if len(text) > STATEMENT_TEXT_MAX_LENGTH:
                        self.fail(
                            '"{}" cannot be longer than {} characters, got {}'.format(
                                text,
                                STATEMENT_TEXT_MAX_LENGTH,
                                len(text)
                            )
                        )

    def test_conversation_format(self):
        files = corpus.list_corpus_files('chatterbot_corpus')

        for dialog_corpus, _categories, _file_path in corpus.load_corpus(*files):
            for conversation in dialog_corpus:
                for text in conversation:
                    if not isinstance(text, str):
                        self.fail('"{}" must be a string, not {}.'.format(
                            str(text),
                            type(text)
                        ))


    def test_language_names(self):
        """
        Each language directory should adhere to the same naming convention.
        """
        valid_language_names = [
            'hinglish'  # This is a special case for Hindi in Latin script
        ]
        language_classes = inspect.getmembers(sys.modules[languages.__name__])

        for _name, obj in language_classes:
            if inspect.isclass(obj):
                valid_language_names.append(obj.ENGLISH_NAME.lower())

        for directory_name in os.listdir(DATA_DIRECTORY):
            self.assertIn(directory_name, valid_language_names)
