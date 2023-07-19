import random
class WordFinder:
    """Word Finder: read a file with each word on a new line from the disk,
    put every word from the file into a list, return the count of the word list
    """
    def __init__(self, file_path):
        """call a method to put each word from the file into a list, and print
        the length of the list"""
        self.file_path = file_path
        self.list_of_words = self.read_file_and_store_words()
        print(f"{len(self.list_of_words)} words read")

    def read_file_and_store_words(self):
        """read the file, return a list of words from the file without /n"""
        f = open(f'{self.file_path}', 'r')

        word_list = []

        for line in f:
            word_list.append(line.strip())

        return word_list

    def random(self):
        """return a random word from the word list"""
        return random.choice(self.list_of_words)

class SpecialWordFinder(WordFinder):
    """Extends WordFinder with a differnt method of parsing a file"""
    def __init__(self,file_path):
        super().__init__(file_path)

    def read_file_and_store_words(self):
        """Read the file,remove any empty line or comments, return the word list"""

        word_list= super().read_file_and_store_words()
        # f = open(f'{self.file_path}', 'r')
        # word_list = []


        # for line in f:
        #     if line.isspace() or line[0]=="#":
        #         continue
        #     else:
        #         word_list.append(line.strip())

        return [word for word in word_list if not word.startswith("#") and word!=""]





