import re
import string
from collections import Counter
from mongodb.mongo_affections_vocabulary import MongoAffectionsVocabulary


class SpellCheck (object):
    def __init__(self, corpus_file_path):
        with open(corpus_file_path, 'r') as file:
            lines = file.readlines()
            words = []
            for line in lines:
                words += re.findall(r'\w+', line.lower())

        self.vocabs = set(words)
        self.vocabs_joined_str = '\t'.join(self.vocabs)
        self.word_counts = Counter(words)
        total_words = float(sum(self.word_counts.values()))
        self.word_probability = {word: self.word_counts[word] / total_words for word in self.vocabs}
        # Database object
        self.mongodb_affections = MongoAffectionsVocabulary()

    def _level_one_edits(self, word):
        letters = string.ascii_lowercase
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [l + r[1:] for l, r in splits if r]
        swaps = [l + r[1] + r[0] + r[2:] for l, r in splits if len(r) > 1]
        replaces = [l + c + r[1:] for l, r in splits if r for c in letters]
        inserts = [l + c + r for l, r in splits for c in letters]
        return set(deletes + swaps + replaces + inserts)

    def _level_two_edits(self, word):
        return set(e2 for e1 in self._level_one_edits(word) for e2 in self._level_one_edits(e1))

    # Underscores delimit multi-word affections, this feature is acceptable up to a maximum of 3 words
    def check_for_underscores(self, word):
        if '_' in word:
            words_array = word.split("_")
            if len(words_array) == 2:
                print('returned', self.check(word.split("_")[0], word.split("_")[1]))
                return self.check(word.split("_")[0], word.split("_")[1])
            else:
                return self.check(word.split("_")[0], word.split("_")[1], word.split("_")[2])
        else:
            return self.check(word)

    def check(self, word, word_1=None, word_2=None):
        # print("word", word, "word_1", word_1, "word_2", word_2)
        # Combinations of current string
        candidates = self._level_one_edits(word) or self._level_two_edits(word) or [word]
        # Check for existing words candidates within our set
        valid_word_candidates = [w for w in candidates if w in self.vocabs]
        database_candidates = []
        if len(valid_word_candidates) != 0:
            # Database
            for valid_word in valid_word_candidates:
                self.mongodb_affections.reset_affections_dictionary()
                self.mongodb_affections.set_words(valid_word, word_1, word_2)
                temporal = self.mongodb_affections.get_affections_dictionary()
                for candidate in temporal:
                    database_candidates.append(candidate.name)

        else:
            # Check for incomplete words
            valid_word_candidates = [w for w in candidates if w in self.vocabs_joined_str]
            for possible_word in valid_word_candidates:
                self.mongodb_affections.reset_affections_dictionary()
                self.mongodb_affections.set_words(possible_word)
                temporal = self.mongodb_affections.get_affections_possibility()
                for candidate in temporal:
                    # Prevent duplicates from entering the list
                    if candidate.name not in database_candidates:
                        database_candidates.append(candidate.name)
        # [item[0] for item in arranged_candidates]
        return database_candidates
