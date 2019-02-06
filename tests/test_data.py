from unittest import TestCase
from chatterbot import corpus
from chatterbot.constants import STATEMENT_TEXT_MAX_LENGTH



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
                            '"{}" cannot be longer than {} characters'.format(
                                text,
                                STATEMENT_TEXT_MAX_LENGTH
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
