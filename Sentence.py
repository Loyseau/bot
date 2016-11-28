from Word import Word

class Sentence:
    def __init__(self, string):
        self.string = string
        self.words = [Word(w) for w in string.split( )]

if __name__ == '__main__':
    phrase = Sentence("Hello my name is")
    print [a.word for a in phrase.words]
    print [a.levenshtein("neme") for a in phrase.words]
    print "ok"