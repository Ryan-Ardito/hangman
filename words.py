import os
import random
import fileinput
from typing import List, Iterable

folder = 'list_files'
min_word_length = 5


def get_words(words_files: List[str]) -> list:
    full_paths = [os.path.join(folder, file) for file in words_files]
    with fileinput.input(files=full_paths, mode='r') as files:
        return make_wordlist(files)


def make_wordlist(files: Iterable) -> list:
    result = set()
    for line in files:
        word = line.strip()
        if not word.isalpha() or len(word) < min_word_length:
            continue
        result.add(word.lower())
    return list(result)


def all_words_files() -> list:
    # Return a list of all .txt files from the wordlists folder
    return [file for file in os.listdir(folder) if file.endswith('.txt')]


class Words:

    def __init__(self, words_files: List[str]):
        """Initialize word buffer, build list of words files."""
        self.words_files = words_files
        self.word_buffer = self.build_buffer()

    def random_word(self) -> str:
        """Pop a random word from word_buffer. If empty, rebuild word_buffer."""
        if not self.word_buffer:
            self.word_buffer = self.build_buffer()
        i = random.randrange(len(self.word_buffer))
        # Avoid repeated words by removing used words
        return self.word_buffer.pop(i)

    def build_buffer(self) -> list:
        # Get a list of clean words
        buffer = get_words(self.words_files)
        if not buffer:
            raise LookupError('No valid words in the provided words files')
        return buffer

