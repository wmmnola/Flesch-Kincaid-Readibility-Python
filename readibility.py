import count_words
k1 = 206.835
k2 = -1.015
k3 = -84.6

def flesch(s):
    num_of_sentances = count_words.count_sentances(s)
    tup = count_words.count_words(s)
    num_of_words = tup[0]
    num_of_syllables = tup[1]
    return k1 + k2 * (num_of_words/num_of_sentances) + k3 *(num_of_syllables/num_of_words)

def read_file():
    f = open("test.txt","r")
    s = f.read()
    print(s)
    print(flesch(s))

read_file()
