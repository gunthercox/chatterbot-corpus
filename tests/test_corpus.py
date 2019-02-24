"""
Tests for the chatterbot corpus package.
"""
import os
import io
from unittest import TestCase
from chatterbot import corpus


class CorpusUtilsTestCase(TestCase):

    def test_get_file_path(self):
        """
        Test that a dotted path is properly converted to a file address.
        """
        path = corpus.get_file_path('chatterbot.corpus.english')
        self.assertIn(
            os.path.join('chatterbot_corpus', 'data', 'english'),
            path
        )

    def test_read_english_corpus(self):
        corpus_path = os.path.join(
            corpus.DATA_DIRECTORY,
            'english', 'conversations.yml'
        )
        data = corpus.read_corpus(corpus_path)
        self.assertIn('conversations', data)

    def test_list_english_corpus_files(self):
        data_files = corpus.list_corpus_files('chatterbot.corpus.english')

        self.assertIn('.yml', data_files[0])

    def test_load_english_corpus(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/english/greetings.yml')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertEqual(len(corpus_data), 1)
        self.assertIn(['Hi', 'Hello'], corpus_data[0][0])

    def test_load_english_corpus_categories(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/english/greetings.yml')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertEqual(len(corpus_data), 1)

        # Test that each conversation gets labeled with the correct category
        for conversation in corpus_data:
            self.assertIn('greetings', conversation[1])


class CorpusLoadingTestCase(TestCase):

    def test_load_corpus_chinese(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/chinese')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_traditional_chinese(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/traditionalchinese')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_english(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/english')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_french(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/french')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_german(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/german')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_hindi(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/hindi')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_indonesian(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/indonesian')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_italian(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/italian')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_marathi(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/marathi')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_portuguese(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/portuguese')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_russian(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/russian')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_spanish(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/spanish')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus_telugu(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/telugu')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))

    def test_load_corpus(self):
        """
        Test loading the entire corpus of languages.
        """
        files = corpus.list_corpus_files('chatterbot_corpus')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))
