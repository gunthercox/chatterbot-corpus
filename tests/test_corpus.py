"""
Tests for the chatterbot corpus package.
"""
import os
from unittest import TestCase
from chatterbot_corpus.corpus import Corpus


class CorpusUtilsTestCase(TestCase):

    def setUp(self):
        self.corpus = Corpus()

    def test_get_file_path(self):
        """
        Test that a dotted path is properly converted to a file address.
        """
        path = self.corpus.get_file_path('chatterbot.corpus.english')
        self.assertIn(
            os.path.join('chatterbot_corpus', 'data', 'english'),
            path
        )

    def test_read_english_corpus(self):
        corpus_path = os.path.join(
            self.corpus.data_directory,
            'english', 'conversations.yml'
        )
        data = self.corpus.read_corpus(corpus_path)
        self.assertIn('conversations', data)

    def test_list_english_corpus_files(self):
        data_files = self.corpus.list_corpus_files('chatterbot.corpus.english')

        self.assertIn('.yml', data_files[0])

    def test_load_corpus(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.english.greetings')

        self.assertEqual(len(corpus), 1)
        self.assertIn(['Hi', 'Hello'], corpus[0])


class CorpusLoadingTestCase(TestCase):

    def setUp(self):
        self.corpus = Corpus()

    def test_load_corpus_chinese(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.chinese')

        self.assertTrue(len(corpus))

    def test_load_corpus_traditional_chinese(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.tchinese')

        self.assertTrue(len(corpus))

    def test_load_corpus_english(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.english')

        self.assertTrue(len(corpus))

    def test_load_corpus_french(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.french')

        self.assertTrue(len(corpus))

    def test_load_corpus_german(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.german')

        self.assertTrue(len(corpus))

    def test_load_corpus_hindi(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.hindi')

        self.assertTrue(len(corpus))

    def test_load_corpus_indonesia(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.indonesia')

        self.assertTrue(len(corpus))

    def test_load_corpus_italian(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.italian')

        self.assertTrue(len(corpus))

    def test_load_corpus_marathi(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.marathi')

        self.assertTrue(len(corpus))

    def test_load_corpus_portuguese(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.portuguese')

        self.assertTrue(len(corpus))

    def test_load_corpus_russian(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.russian')

        self.assertTrue(len(corpus))

    def test_load_corpus_spanish(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.spanish')

        self.assertTrue(len(corpus))

    def test_load_corpus_telugu(self):
        corpus = self.corpus.load_corpus('chatterbot.corpus.telugu')

        self.assertTrue(len(corpus))
