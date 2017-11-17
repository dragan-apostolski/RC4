from collections import Counter
from operator import itemgetter


def get_letter_frequencies(ciphered_text):
    ciphered_text = list(filter(lambda c: c.isalpha(), ciphered_text))
    return dict(Counter(ciphered_text))


englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
eng_letters_sorted = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']


file = open('/home/drapostolski/PycharmProjects/LearningPython/cryptography/encrypted_text.txt', 'r')
text = file.readlines()
file.close()
ciphered_text = ""
for line in text:
    ciphered_text += line

ciphered_text = ciphered_text.replace('\n', ' ')
print(ciphered_text)

letter_frequencies = [(l, f) for (l, f) in get_letter_frequencies(ciphered_text).items()]
letter_frequencies.append(('z', 0))
letter_frequencies.sort(key=itemgetter(1), reverse=True)
just_letters = [l for (l, f) in letter_frequencies]

print(list(zip(just_letters, eng_letters_sorted)))

#[('r', 'E'), ('b', 'T'), ('m', 'A'), ('k', 'O'), ('j', 'I'), ('w', 'N'), ('i', 'S'), ('p', 'H'),
# ('u', 'R'), ('h', 'D'), ('d', 'L'), ('v', 'C'), ('x', 'U'), ('y', 'M'), ('s', 'W'), ('n', 'F'), ('t', 'G'),
# ('l', 'Y'), ('q', 'P'), ('o', 'B'), ('e', 'V'), ('a', 'K'), ('c', 'J'), ('f', 'X'), ('g', 'Q'), ('z', 'Z')]
