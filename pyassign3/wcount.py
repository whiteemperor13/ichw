#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Xiangtao Hu"
__pkuid__  = "1700011768"
__email__  = "white_emperor@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import string

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    d={}
    t=[]
    for i in string.punctuation+string.whitespace:
        lines=lines.split(i)
    for word in lines:
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
    numbers=sorted(d.values(),reverse=True)
    for i in range(len(numbers)):
        if len(t)==topn:
            break
        for word in d:
            if d[word]==numbers[i]:
                t.append(word)
            if len(t)==topn:
                break
    for word in t:
        print(word,d[word])

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)