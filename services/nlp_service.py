from nltk import word_tokenize
from nltk.corpus import wordnet
from random import randrange

crypted = {}


def encrypt(text_encrypt: str) -> str:
    encrypt_text_as_list = text_encrypt.split()

    shakespear_tokens = list(set(get_romeo_juliet_data_tokenized()))
    crypt_list = []

    for word in encrypt_text_as_list:
        result_from_compare = get_closest_word_for_word(word, shakespear_tokens)
        crypt_list.append(result_from_compare[1])

    return " ".join(crypt_list)


def decrypt(text_decrypt: str) -> str:
    result_list = []
    for word in text_decrypt.split():
        try:
            result_list.append(crypted[word])
        except KeyError:
            raise ValueError("This text was not encrypted.")

    return " ".join(result_list)


def get_closest_word_for_word(word_to_compare: str, shakespear_tokens: list):
    init_value = -9999
    closest_word = "heck"
    for token_to_compare in shakespear_tokens:
        to_compare = wordnet.synsets(word_to_compare)
        from_compare = wordnet.synsets(token_to_compare)
        if to_compare and from_compare and to_compare != from_compare:
            result = to_compare[0].wup_similarity(from_compare[0])

            if init_value < result:
                closest_word = token_to_compare
                init_value = result

    if init_value == -9999:
        closest_word = shakespear_tokens[randrange(len(shakespear_tokens))]

    crypted[closest_word] = word_to_compare
    return init_value, closest_word


def get_romeo_juliet_data_tokenized() -> list:
    f = open('data/romeoAndJuliet.txt', 'r')
    text_as_string = ""
    for line in f.readlines():
        text_as_string += line
    return [word.lower() for word in word_tokenize(text_as_string)]
