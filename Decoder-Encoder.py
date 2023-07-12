def get_random_char(seed, char):
    prime_number = 31
    random_seed = seed % 2**32
    while True:
        random_seed = (random_seed * 1103515245 + 12345) % 2**32
        random_char = chr((random_seed + ord(char) * prime_number) % 95 + 32)
        if random_char != char:
            return random_char

def encode_message(message, key):
    encoded_message = ""
    char_map = {}

    for char in message:
        if char not in char_map:
            random_char = get_random_char(key, char)
            char_map[char] = random_char
        encoded_message += char_map[char]

    return encoded_message


def decode_message(encoded_message, char_map):
    decoded_message = ""

    for char in encoded_message:
        if char in char_map:
            decoded_message += char_map[char]
        else:
            decoded_message += char

    return decoded_message


message = input("Enter your text: ")
key = 5

encoded_message = encode_message(message, key)
print("Encoded message:", encoded_message)

char_map = {v: k for k, v in zip(message, encoded_message)}
decoded_message = decode_message(encoded_message, char_map)
print("Decoded message:", decoded_message)

