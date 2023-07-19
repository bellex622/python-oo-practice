class WordFinder:
    """Word Finder: finds random words from a dictionary
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.list_of_words = self.read_file_and_store_words()
        print(f"{len(self.list_of_words)} words read")

    def read_file_and_store_words(self):
        f = open(f'{self.file_path}', 'r')

        word_list = []

        for line in f:
            word_list.append(line.strip())

        return word_list

"""
instantiated with path to file containing one word per line
read file, makes attribute of list of those words
prints out '[num-of-words-read] words read'

**remove \n from each word**
(doesn't all have to be in init)

has method random() that returns random word from list
(should not re-read list each time, works with already read list)
can use: /usr/share/dict/words


"""


