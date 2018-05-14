import os


DIALOG_MAXIMUM_CHARACTER_LENGTH = 400


class CorpusObject(list):
    """
    This is a proxy object that allow additional
    attributes to be added to the collections of
    data that get returned by the corpus reader.
    """

    def __init__(self, *args, **kwargs):
        """
        Imitate a list by allowing a value to be passed in.
        """
        if args:
            super(CorpusObject, self).__init__(args[0])
        else:
            super(CorpusObject, self).__init__()

        self.categories = []


class Corpus(object):

    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.data_directory = os.path.join(current_directory, 'data')

    def get_file_path(self, dotted_path, extension='json'):
        """
        Reads a dotted file path and returns the file path.
        """

        # If the operating system's file path seperator character is in the string
        if os.sep in dotted_path or '/' in dotted_path:
            # Assume the path is a valid file path
            return dotted_path

        parts = dotted_path.split('.')
        if parts[0] == 'chatterbot':
            parts.pop(0)
            parts[0] = self.data_directory

        corpus_path = os.path.join(*parts)

        if os.path.exists(corpus_path + '.{}'.format(extension)):
            corpus_path += '.{}'.format(extension)

        return corpus_path

    def read_corpus(self, file_name):
        """
        Read and return the data from a corpus json file.
        """
        import io
        import yaml

        with io.open(file_name, encoding='utf-8') as data_file:
            data = yaml.load(data_file)
        return data

    def list_corpus_files(self, dotted_path):
        """
        Return a list of file paths to each data file in
        the specified corpus.
        """
        CORPUS_EXTENSION = 'yml'

        corpus_path = self.get_file_path(dotted_path, extension=CORPUS_EXTENSION)
        paths = []

        if os.path.isdir(corpus_path):
            for dirname, dirnames, filenames in os.walk(corpus_path):
                for datafile in filenames:
                    if datafile.endswith(CORPUS_EXTENSION):
                        paths.append(os.path.join(dirname, datafile))
        else:
            paths.append(corpus_path)

        paths.sort()
        return paths

    def load_corpus(self, dotted_path):
        """
        Return the data contained within a specified corpus.
        """
        data_file_paths = self.list_corpus_files(dotted_path)

        corpora = []

        for file_path in data_file_paths:
            corpus = CorpusObject()
            corpus_data = self.read_corpus(file_path)

            conversations = corpus_data.get('conversations', [])
            corpus.categories = corpus_data.get('categories', [])
            corpus.extend(conversations)

            corpora.append(corpus)

        return corpora
