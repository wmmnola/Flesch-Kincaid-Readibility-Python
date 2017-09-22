import re
import syllables

def count_words(s):
    count = 0;
    l = s.split(" ")
    count = len(l)
    syll_count = 0
    for word in l:
        syll_count += syllables.numsyllables(word)[0]
    return (count,syll_count)

def count_sentances(s):
    replaced_string = (s.replace('?','.').replace("!","."))
    l = replaced_string.split(".")
    l.pop(len(l)-1)
    return len(l)
