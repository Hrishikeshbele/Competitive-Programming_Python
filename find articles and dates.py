'''
given an text find all articles and dates in paragraph.

'''
import sys
import re

def count_element(line):
    delimiters = re.compile(r'[,.(); "\']')
    words = delimiters.split(line)
    #print(words)

    # Number of "a"
    print(words.count('a')+words.count('A'))

    # Number of "an"
    print(words.count('an')+words.count('An'))

    # Number of "the"
    print(words.count('the')+words.count('The'))

    # Number of dates
    month = r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|[0-9]{1,2})'
    day = r'([0-9]{1,2}(st|nd|rd|st)?)'
    prep = r'((of)?)'
    year = r'([0-9]{1,4})'

    format = [r'({}/{}/{})'.format(month, day, year),
              r'({}/{}/{})'.format(day, month, year),
              r'({} {}[ ,]*{})'.format(month, day, year),
              r'({} {}[ ,]*{})'.format(day, month, year),]
    #print(len(re.findall(r'|'.join(format), line)))
    print(len(re.finditer(r'|'.join(format), line)))
    print((re.finditer(r'|'.join(format), line)))

def main():
    n = input()
    for line in sys.stdin:
        line = line.strip()
        if line:
            count_element(line)
