import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenizeinput_file = open('req-parse.txt').read()
type(input_file)text = input_file #where input file is any input file
print()
print("----------------------------------------------------------------")
print("This tokenization prints all words including punctuation marks")
print("----------------------------------------------------------------")
words_from_sentence = word_tokenize(text)
print(word_tokenize(text))
print()print()
print("---------------------------------------------------------")
print("This prints all words with associated part of speech")
print("---------------------------------------------------------")
parts_of_speech = nltk.pos_tag(words_from_sentence)
print(parts_of_speech)

# insert statistics from feedback from the output of the initial code
# using both the PoS statistics and the classifier, we can build a confusion matrix
