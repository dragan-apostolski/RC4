from operator import itemgetter
from collections import Counter
import csv


def get_letter_frequencies(text):
    return dict(Counter(text))


def get_letter_pairs_frequencies(text):
    tuple_frequencies = {}
    for i in range(0, len(text) - 1):
        c1 = text[i]
        c2 = text[i + 1]
        tuple_frequencies.setdefault((c1, c2), 0)
        tuple_frequencies[(c1, c2)] += 1
    return tuple_frequencies


def read_alphabet_frequencies(path_to_file):
    tuple_frequencies = []
    with open(path_to_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            tuple_frequencies.append(tuple(row))
    return tuple_frequencies


alphabet_freqs = read_alphabet_frequencies('cryptography/lab1/frekvencii.tsv')
alphabet_pairs_freqs = read_alphabet_frequencies('cryptography/lab1/parovi_frekvencii.tsv')

file = open('cryptography/lab1/141020_encrypted_text', 'r')
enc_text = file.readlines()[0]
file.close()

freq_list_pairs = [(tup, freq) for (tup, freq) in get_letter_pairs_frequencies(enc_text).items()]
freq_list_letters = [(let, round(freq/len(enc_text)*100, 2)) for (let, freq) in get_letter_frequencies(enc_text).items()]

freq_list_pairs.sort(key=itemgetter(1), reverse=True)
freq_list_letters.sort(key=itemgetter(1), reverse=True)


print(freq_list_letters)
print("\n")
print(alphabet_freqs)

print("\n")
print(freq_list_pairs)