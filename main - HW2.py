''' main.py
    Do NOT modify this file!
'''
from hwcode import *
import numpy as np

def main():
    # Exercise 1 : Part 1
    '''positive_words = set()
    negative_words = set()
    with open('./data/bing_liu/negative-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            negative_words.add(row.strip())
    with open('./data/bing_liu/positive-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            positive_words.add(row.strip())

    print("EXERCISE 1:")
    macro_f1 = classify_tweets_lexicon('./data/trainTwitterData.csv', positive_words, negative_words)
    
    try:
        assert(type(macro_f1) is float)
    except:
        print("ERROR: classify_tweets_lexicon should return an float")

    # Exercise 1 : Part 2
    macro_f1_svm = classify_tweets('./data/trainTwitterData.csv')
    try:
        assert(type(macro_f1_svm) is float)
    except:
        print("ERROR: classify should return an float")

    print("lexicon F1: {:.4f} SVM F1: {:.4f}".format(macro_f1, macro_f1_svm))
    print()

    # Exercise 2 : Part 1
    macro_f1_feats = hospital_p1('./data/colon_data.csv')
    try:
        assert(type(macro_f1_feats) is float)
    except:
        print("ERROR: hospital_p1 should return an float")

    print("Colon F1: {:.4f}".format(macro_f1_feats))

    # Exercise 2 : Part 2
    best_feats = hospital_p2('./data/colon_data.csv')
    try:
        assert(type(best_feats) is list)
    except:
        print("ERROR: hosptial_p2 should return a list")
    try:
        assert(len(best_feats) == 5)
    except:
        print("ERROR: hospital_p2 should return a list of length 5")

    print("Best Colong Feats: {}".format(best_feats))
    print()


    # Extra Credit 1
    print("EXTRA CREDIT:")
    better_macro_f1 = better_model('./data/trainTwitterData.csv')
    try:
        assert(type(better_macro_f1) is float)
    except:
        print("ERROR: better_model should return an float")
    try:
        assert(better_macro_f1 > macro_f1_svm)
    except:
        print("ERROR: You need to improve on Exercise 1 Part 2!")
    print("EX 1 P1 F1: {:.4f} Extra Credit F1: {:.4f}".format(macro_f1_svm, better_macro_f1))

    print()'''
    print("EXTRA EXTRA CREDIT:")
    comp  = competition('./data/trainTwitterData.csv', './data/fakeTwitterTest.csv')
    try:
        assert(type(comp) is np.ndarray)
    except:
        print("ERROR: competition should return a numpy array")


if __name__ == '__main__':
    main()
