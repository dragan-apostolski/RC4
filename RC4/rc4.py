
class StateVector:
    """Оваа класа го опишува векторот на состојба - s, кој во секое време содржи пермутација на сите 8-битни броеви во
    опсегот [0 - 255]"""

    def __init__(self, initial_key):
        """Во конструкторот на векторот на состојба се пополнува идентичната пермутација на s, се креира помошен вектор
        t - ги содржи вредностите на иницијалниот клуч, и се прави првичната пермутација на s, која зависи од
        вредностите на иницијалниот клуч

        :param initial_key низа од бајти со вредности на почетниот клуч
        """
        self.key_length = len(initial_key)
        self.s = list(range(256))  # identity permutation
        self.t = [initial_key[i % self.key_length] for i in range(256)]
        self.__permutate_state_vector__()

    def __permutate_state_vector__(self):
        """Во оваа функција се прави првичната пермутација на векторот на состојба - s. Бидејќи единствената операција е
        swap, резултатот е повторно пермутација.
        """
        j = 0
        for i in range(256):
            j = (j + self.s[i] + self.t[i]) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]

    def swap(self, i, j):
        """Ги заменува вредностите од s на позициите i и j"""
        self.s[i], self.s[j] = self.s[j], self.s[i]

    def __getitem__(self, item):
        return self.s[item]


def generate_key_stream(key, offset=0, length=16):
    """Оваа функција генерира keystream со должина length, врз основа на иницијалниот клуч key. Прво се иницијализира
    објект од класата StateVector, кој што ќе биде енкапсулација на векторот на состојба s. Вредностите (бајтите) за
    keystream-от се случајно избрани вредности од векторот на состојба, а по секоја избрана вредност за клучот се врши
    нова пермутација на s со повик на функцијата swap

    :param key: низа од бајти со вредностите на клучот
    :param offset: после која позиција да почнат да се користат бајтите на клучот
    :param length: должина на клучот
    :return генератор објект кој ги содржи вредностите на keystream-от во форма на цели броеви од опсегот [0 - 255]
    """
    state_vector = StateVector(key)
    i = j = 0
    count = 0
    while count < length + offset:
        i = (i + 1) % 256
        j = (j + state_vector[i]) % 256
        state_vector.swap(i, j)
        if count >= offset:
            yield (state_vector[(state_vector[i] + state_vector[j]) % 256])
        count += 1


def encrypt(plain_text, key, offset=0):
    """Примитивата encrypt служи за енкриптирање на текстот даден во plain_text со клуч key.

    :param plain_text: bytes објект од карактерите на оригиналниот текст
    :param key: хексадецимален стринг кој претставува клуч за шифрирањето
    :param offset: после која позиција да почнат да се користат бајтите на клучот
    :return хексадецимален стринг кој претставува шифриран текст со клуч key
    """
    cipher_text = ''
    key_stream = generate_key_stream(bytearray.fromhex(key), offset, len(plain_text))
    for c in plain_text:
        letter = ("%02X" % (c ^ next(key_stream)))
        cipher_text += letter
    return cipher_text


def decrypt(ciphered_text, key, offset=0):
    """Примитивата decrypt служи за дешифрирање на шифрираниот текст ciphered_text со клуч key.

    :param ciphered_text: хексадецимален стринг, вратен од повик на функцијата encrypt со клуч key и офсет offset
    :param key: клучот за дешифрирање на пораката
    :param offset: после која позиција да почнат да се користат бајтите на клучот
    :return дешифриран текст во форма на bytes објект
    """
    original = ''
    ciphered_text = bytearray.fromhex(ciphered_text)
    key_stream = generate_key_stream(bytearray.fromhex(key), offset, len(ciphered_text))
    for i in range(len(ciphered_text)):
        original += chr(ciphered_text[i] ^ next(key_stream))
    return bytes(original.encode('utf-8'))


def print_key_stream_in_hex(ks_arr):
    for c in ks_arr:
        print('{:02x} '.format(c), end="")
    print()


def process_test_vector(test_vector):
    offsets = [0, 16, 240, 256, 496, 512, 752, 768, 1008, 1024, 1520, 1536, 2032, 2048, 3056, 3072, 4080, 4096]
    print("Key: 0x{:<64}\tLength in bits: {:<3}".format(test_vector, int(len(test_vector)/2 * 8)))
    for offset in offsets:
        key_stream = generate_key_stream(bytearray.fromhex(test_vector), offset)
        print('Offset={:<22}\tKey stream:'.format(offset), end='\t')
        print_key_stream_in_hex(list(key_stream))
    print()


def main():
    with open('test_vectors') as f:
        lines = f.readlines()
    for line in lines:
        process_test_vector(line[0:len(line)-1])


if __name__ == '__main__':
    main()
