import numpy.random as np


file = open("cryptography/lab1/156010_plain_text", 'r')
lines = file.readlines()
file.close()
text = ""
for line in lines:
    text += line
full_text = ""

for char in list(filter(lambda c: c.isalpha(), text)):
    full_text += char.lower()

print(full_text)

alphabet = ['а', 'б', 'в', 'г', 'д', 'ѓ', 'е', 'ж', 'з', 'ѕ', 'и', 'ј', 'к', 'л', 'љ', 'м', 'н', 'њ', 'о', 'п', 'р',
            'с', 'т', 'ќ', 'у', 'ф', 'х', 'ц', 'ч', 'џ', 'ш']
permuted_alphabet = list(np.permutation(alphabet))
mappings = {o: p for (o, p) in zip(alphabet, permuted_alphabet)}

encrypted_text = ""
for c in full_text:
    encrypted_text += mappings[c]

file = open("cryptography/lab1/156010_encrypted_text", 'w')
file.writelines(encrypted_text)


# текстот беше енкриптиран со оваа пермутација:
# {'в': 'џ', 'ф': 'л', 'џ': 'у', 'з': 'а', 'у': 'њ', 'ц': 'о', 'ж': 'ч', 'р': 'в', 'ш': 'ѓ', 'г': 'р', 'и': 'ќ', 'м': 'з', 'љ': 'ф', 'ќ': 'м', 'ч': 'к', 'к': 'ш', 'п': 'д', 'д': 'б', 'с': 'п', 'њ': 'ц', 'х': 'г', 'а': 'т', 'ѕ': 'ј', 'о': 'ж', 'л': 'е', 'е': 'х', 'б': 'ѕ', 'ј': 'н', 'ѓ': 'с', 'н': 'љ', 'т': 'и'}
