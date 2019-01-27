from unittest import TestCase
from chatterbot_corpus import corpus


class CorpusUtilsTestCase(TestCase):
    """
    This test case is designed to make sure that all
    corpus data adheres to a few general rules.
    """

    def test_character_count(self):
        """
        Test that no line in the corpus exceeds the
        maximum number of characters.
        """
        from chatterbot_corpus.corpus import DIALOG_MAXIMUM_CHARACTER_LENGTH

        corpora = corpus.load_corpus('chatterbot.corpus')

        for conversations in corpora:
            for conversation in conversations:
                for statement in conversation:
                    if len(statement) > DIALOG_MAXIMUM_CHARACTER_LENGTH:
                        self.fail(
                            '"{}" cannot be longer than {} characters'.format(
                                statement,
                                DIALOG_MAXIMUM_CHARACTER_LENGTH
                            )
                        )

    def test_conversation_format(self):
        corpora = corpus.load_corpus('chatterbot.corpus')

        for conversations in corpora:
            for conversation in conversations:
                for text in conversation:
                    if not isinstance(text, str):
                        self.fail('"{}" must be a string, not {}.'.format(
                            str(text),
                            type(text)
                        ))
