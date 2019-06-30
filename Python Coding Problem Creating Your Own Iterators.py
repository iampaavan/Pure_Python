class Sentence:

    def __init__(self, string):
        self.string = string
        self.index = 0
        self.words = self.string.split()

    def __repr__(self):
        return f"Class Object: data = {self.string}."

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.words):
            raise StopIteration

        index = self.index
        self.index += 1
        return self.words[index]


def my_func(sentence):
    for words in sentence.split():
        yield words


my_sentence = Sentence('This is a sentence')
# print(my_sentence)

for word in my_sentence:
    print(word)



