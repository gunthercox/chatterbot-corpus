from unittest import TestCase
import os
from corpus.corpus import Corpus

class CorpusUtilsTestCase(TestCase):

    def setUp(self):
        self.corpus = Corpus()

    def test_get_file_path(self):
        """
        Test that a dotted path is properly converted to a file address.
        """
        path = self.corpus.get_file_path('corpus.data.english')
        self.assertIn(
            os.path.join('corpus', 'data', 'english'),
            path
        )

    def test_read_english_corpus(self):
        corpus_path = os.path.join(
            'corpus', 'data', 'english', 'conversations.corpus.json'
        )
        data = self.corpus.read_corpus(corpus_path)
        self.assertIn('conversations', data)

    def test_list_english_corpus_files(self):
        data_files = self.corpus.list_corpus_files('corpus.data.english')

        self.assertIn('.json', data_files[0])

    def test_load_corpus(self):
        corpus = self.corpus.load_corpus('corpus.data.english.greetings')

        self.assertEqual(len(corpus), 1)
        self.assertIn(['Hi', 'Hello'], corpus[0])

    def test_load_corpus_english(self):
        corpus = self.corpus.load_corpus("corpus.data.english")
        self.assertEqual(len(corpus), 18)
        self.assertIn(corpus[1], corpus)


class CorpusLoadingTestCase(TestCase):

    def setUp(self):
        self.corpus = Corpus()

    def test_load_corpus_chinese(self):
        corpus = self.corpus.load_corpus('corpus.data.chinese')

        self.assertTrue(len(corpus))

    def test_load_corpus_traditional_chinese(self):
        corpus = self.corpus.load_corpus('corpus.data.tchinese')

        self.assertTrue(len(corpus))

    def test_load_corpus_english(self):
        corpus = self.corpus.load_corpus('corpus.data.english')

        self.assertTrue(len(corpus))

    def test_load_corpus_french(self):
        corpus = self.corpus.load_corpus('corpus.data.french')

        self.assertTrue(len(corpus))

    def test_load_corpus_german(self):
        corpus = self.corpus.load_corpus('corpus.data.german')

        self.assertTrue(len(corpus))

    def test_load_corpus_hindi(self):
        corpus = self.corpus.load_corpus('corpus.data.hindi')

        self.assertTrue(len(corpus))

    def test_load_corpus_indonesia(self):
        corpus = self.corpus.load_corpus('corpus.data.indonesia')

        self.assertTrue(len(corpus))

    def test_load_corpus_italian(self):
        corpus = self.corpus.load_corpus('corpus.data.italian')

        self.assertTrue(len(corpus))

    def test_load_corpus_marathi(self):
        corpus = self.corpus.load_corpus('corpus.data.marathi')

        self.assertTrue(len(corpus))

    def test_load_corpus_portuguese(self):
        corpus = self.corpus.load_corpus('corpus.data.portuguese')

        self.assertTrue(len(corpus))

    def test_load_corpus_russian(self):
        corpus = self.corpus.load_corpus('corpus.data.russian')

        self.assertTrue(len(corpus))

    def test_load_corpus_spanish(self):
        corpus = self.corpus.load_corpus('corpus.data.spanish')

        self.assertTrue(len(corpus))

    def test_load_corpus_telugu(self):
        corpus = self.corpus.load_corpus('corpus.data.telugu')

        self.assertTrue(len(corpus))
