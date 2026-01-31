import os
import sys
import inspect
import yaml
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
        failures = []
        max_length = 0

        for dialog_corpus, _categories, _file_path in corpus.load_corpus(*files):
            line_number = 0
            for conversation in dialog_corpus:
                for text in conversation:
                    line_number += 1
                    if len(text) > STATEMENT_TEXT_MAX_LENGTH:
                        max_length = max(max_length, len(text))
                        truncated_text = text[:100] + '...' if len(text) > 100 else text
                        failures.append(
                            'File: {}\nLine: {}\nContent: "{}"\nError: Cannot be longer than {} characters, got {}'.format(
                                _file_path,
                                line_number,
                                truncated_text,
                                STATEMENT_TEXT_MAX_LENGTH,
                                len(text)
                            )
                        )

        if failures:
            self.fail('\n\n'.join(failures + ['\nTotal: {} lines exceeding character limit (max length: {})'.format(len(failures), max_length)]))

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

    def test_yaml_keys_are_english(self):
        """
        Test that all YAML corpus files use English keys 'categories' and 'conversations'
        rather than localized translations, ensuring consistent parsing across languages.
        """
        for language_dir in os.listdir(DATA_DIRECTORY):
            language_path = os.path.join(DATA_DIRECTORY, language_dir)

            if not os.path.isdir(language_path):
                continue

            for filename in os.listdir(language_path):
                if not filename.endswith('.yml'):
                    continue

                file_path = os.path.join(language_path, filename)

                with open(file_path, 'r', encoding='utf-8') as file:
                    try:
                        data = yaml.safe_load(file)

                        # Check that 'categories' key exists (not localized variants)
                        self.assertIn(
                            'categories',
                            data,
                            f'{file_path} must use "categories" key (not localized)'
                        )

                        # Check that 'conversations' key exists (not localized variants)
                        self.assertIn(
                            'conversations',
                            data,
                            f'{file_path} must use "conversations" key (not localized)'
                        )

                        # Ensure no common localized variants are used
                        localized_keys = [
                            'kategori', 'percakapan',  # Indonesian
                            'categorias', 'conversaciones',  # Spanish
                            'kategorien', 'gesprache',  # German
                            'категории', 'разговоры',  # Russian
                            'catégories', 'conversations',  # French (conversations same)
                        ]

                        for key in localized_keys:
                            if key in ['conversations']:  # Skip English words
                                continue
                            self.assertNotIn(
                                key,
                                data,
                                f'{file_path} should not use localized key "{key}"'
                            )
                    except yaml.YAMLError as e:
                        self.fail(f'YAML parsing error in {file_path}: {e}')

