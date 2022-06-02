

from random import choice


class WordFinder:

    """Word Finder: finds random words from a text file containing a list of words.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    """

    def __init__(self, filepath):
        self.wordlist = self.create_wordlist(filepath)
        print(f"{len(self.wordlist)} words read")

    """creates a wordlist by parsing words from lines in a txt file"""

    def create_wordlist(self, filepath):
        file = open(filepath)
        wordlist = [line.strip() for line in file]
        file.close()
        return wordlist

    """returns a random word from the wordlist"""

    def random(self):
        return choice(self.wordlist)


class SpecialWordFinder(WordFinder):

    """an extension of the WordFinder class which filters out blank lines and comments from the words file.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def create_wordlist(self, filepath):
        file = open(filepath)
        wordlist = [line.strip() for line in file if line.strip()
                    and not line.startswith('#')]
        file.close()
        return wordlist
