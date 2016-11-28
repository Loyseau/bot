class Word:
    def __init__(self, string):
        self.word = string
        self.category = ""

    @staticmethod
    def iter_list(l, i, m, m_):
        l_ = [i]
        for j in range(len(l) - 1):
            l_.append(min(l_[j] + 1, l[j + 1] + 1, l[j] + (m[i - 1] != m_[j])))
        return l_

    def levenshtein(self, m):
        l = [a for a in range(len(m) + 1)]
        for i in range(1, len(self.word) + 1):
            l = self.iter_list(l, i, self.word, m)
        return l[-1]

