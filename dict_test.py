def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    print(frequency)    
    return frequency

def read_words(filename):
    print(open(filename).read().split())
    return open(filename).read().split()

def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in sorted(frequency.items(),reverse=True):
        print(word, count)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])

