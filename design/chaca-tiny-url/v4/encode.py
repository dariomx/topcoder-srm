ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"

# dictionary which assigns a base-digit to each letter in alphabet
ALPHA_DEC = dict(map(reversed, enumerate(ALPHABET)))

# encoding of an integer (from a sequence): changes of base the integer,
# using as target base the length of the alphabet. uses the letters from
# alphabet instead of base-digits (for brevity). the encoding generates
# the base-digits in reverse order (cheaper processing).
def encode_seq(seq):
    base = len(ALPHABET)
    seq_b = []
    rem = seq
    while rem > base:
        seq_b.append(ALPHABET[rem % base])
        rem = rem / base
    if rem > 0:
        seq_b.append(ALPHABET[rem])
    return ''.join(seq_b)

# inverse operation of encode_seq: given the encoded version of the sequence,
# it converts it back into an integer (base 10)
def decode_seq(seq_b):
    base = len(ALPHABET)
    pow_base = 1
    seq = 0
    for letter in seq_b:
        seq += pow_base * ALPHA_DEC[letter]
        pow_base *= base
    return seq
