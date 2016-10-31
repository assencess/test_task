#!/usr/bin/env python3
import sys

def count_sentences_words(string):
    '''
    Function returns two variables. First is number of
    words in string, second is number of sentences 
    divided by dote in string.
    '''
    words = string[:].split()
    sentences = string[:].split('.')

    number_words = len(list(filter(None, words)))
    number_sentences = len(list(filter(None, sentences)))
    
    return number_words, number_sentences

if __name__ == '__main__':
    # words - 8, sentences - 6
    string = "Test. Test Test. Test. Test. Test. Test Test."
    # 'cause string arg is second argument(first is name of file)
    if len(sys.argv) != 1:
        string = sys.argv[1]

    words, sentences = count_sentences_words(string)
    print("Words: {}\nSentences: {}".format(words, sentences))