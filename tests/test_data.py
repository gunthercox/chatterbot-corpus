from __future__ import unicode_literals
from unittest import TestCase
from chatterbot_corpus.corpus import Corpus


class CorpusUtilsTestCase(TestCase):
    """
    This test case is designed to make sure that all
    corpus data adheres to a few general rules.
    """

    def setUp(self):
        self.corpus = Corpus()

    def test_character_count(self):
        """
        Test that no line in the corpus excedes the
        maximum number of characters.
        """
        from chatterbot_corpus.corpus import DIALOG_MAXIMUM_CHARACTER_LENGTH

        corpora = self.corpus.load_corpus('chatterbot.corpus')

        for converstions in corpora:
            for conversation in converstions:
                for statement in conversation:
                    if len(statement) > DIALOG_MAXIMUM_CHARACTER_LENGTH:
                        self.fail(
                            u'"{}" cannot be longer than {} characters'.format(
                                statement,
                                DIALOG_MAXIMUM_CHARACTER_LENGTH
                            )
                        )
