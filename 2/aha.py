import math

# B. Rotate a one-dimensional vector of n elements left by i positions.
def rotate_vector(vector, n):
    """shift all elements to the left by N places, wrapping.

    Think of this array as two arrays, a and b.  We want to
    convert ab to ba.  If we reverse each subarray, we have a'b'.
    Reverse the entire thing and we have ba.  This is great because
    we don't need to copy into another array and it runs in O(n) time.
    """
    reverse_sublist(vector, 0, n)
    reverse_sublist(vector, n, len(vector))
    reverse_sublist(vector, 0, len(vector))

def reverse_sublist(vector, start, end):
    """Helper function to reverse the elements from start to end."""
    endrange = math.ceil((end - start) / 2)

    for i in range(0, endrange):
        dest = end - i - 1
        vector[start + i], vector[dest] = vector[dest], vector[start + i]


# C. Given a list of words, find all the sets anagrams.
# 
def find_anagrams_hash(wordlist):
    """Given a list of words, will return a list of lists of anagrams.

    Create a canonical form by sorting the letters alphabetically, and store in a hash table.""" 
    anagram_table = {}

    for word in wordlist:
        key = hash_word(word)
        if key not in anagram_table:
            anagram_table[key] = [word]
        else:
            anagram_table[key].append(word)

    # screen out all the solo values as they are not anagrams
    return [ v for v in anagram_table.values() if len(v) > 1]

def hash_word(word):
    return ''.join(sorted([l for l in word]))

if __name__ == '__main__':

    vector =  [ 1, 2, 3, 4, 5, 6]
    rotate_vector(vector, 2)
    print(vector)

    print(find_anagrams_hash(['top','pot','beetle','stop','pots']))