import statistics
class TextInfo:


    def __init__(self):
        
        self.text = ""
        self.sentences = []
        self.sentence_count = 0
        self.dictionary = {}
        self.word_count = 0
        self.word_in_sentence_count = []
        self.average_word_amount = 0
        self.median_word_amount = 0
        self.n_grams = {}
        
        self.text_input()
        self.split_into_sentences()
        self.split_into_words()
        self.average_word_amount = self.word_count/self.sentence_count
        self.median_word_amount = statistics.median(self.word_in_sentence_count)
        self.n_gram()


    def text_input(self):
        self.text = input("Please input whole sentence:")
        self.text = self.text.replace('!', '.')
        self.text = self.text.replace('?', '.')
        self.text = self.text.replace(',', ' ')
        self.text = self.text.replace('-', '')
        self.text = self.text.lower()
        pass

    def split_into_sentences(self):
        self.sentences = self.text.split('.')
        for s in self.sentences:
            self.word_in_sentence_count.append(0)
            self.sentence_count += 1
        pass

    def split_into_words(self):
        i = -1
        for sentence in self.sentences:
            i += 1
            words = sentence.split()
            for w in words:
                self.word_count += 1
                self.word_in_sentence_count[i] += 1
                if w in self.dictionary.keys():
                    self.dictionary[w] += 1
                else:
                    self.dictionary[w] = 1
        pass

    def n_gram(self):
        i = 0
        n = int(input("Enter n for n-gram:"))
        temp_text = self.text.replace(' ', '')
        temp_list = []
        while i <= len(temp_text) - n:
            temp_list.append(temp_text[i:i+n])
            i += 1
        for g in temp_list:
            if g in self.n_grams.keys():
                self.n_grams[g] += 1
            else:
                self.n_grams[g] = 1
        pass


    def print_all_info(self):
        print("sentences:", self.sentences)
        print("amount of sentences", self.sentence_count)
        print("amount of words", self.word_count)
        print("text dictionary", self.dictionary)
        for i in self.word_in_sentence_count:
            print("there're ", i, " words in the ", self.word_in_sentence_count.index(i)+1,  " sentence")
        print("average word amount:", self.average_word_amount)
        print("median word amount", self.median_word_amount)
        print("n-grams:", self.n_grams)
        pass
