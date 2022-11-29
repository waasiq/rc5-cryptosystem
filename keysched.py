import rc5 

#* Code for the key scheduler for RC5 algorithm

p = 0xb7e15163  # For 32 bit words
q = 0x9e3779b9  # For 32 bit words

def sub_key_scheduler(rounds):
    key_list = []
    key_list.append(p)
    for i in range(1, 2*rounds + 2):
        key_list.append((key_list[i-1] + q) % 2**32)
    return key_list

def main_key_scheduler(key, rounds):
    bin_key = rc5.text_to_binary(key)
    
    key_len = len(bin_key)
    if (key_len > 2040):
        print('Key length cant be more than 255 bytes')
        exit()

    byte_key = rc5.divide_into_1_byte(bin_key)
    word_key = rc5.divide_into_words(bin_key)


    key_list = sub_key_scheduler(rounds)
    A = B = 0
    i = j = 0
    v = 3 * max(len(word_key), 2*rounds + 2)

    for s in range(v):
        A = key_list[i] = (key_list[i] + A + B) % 2**32
        B = word_key[j] = (word_key[j] + A + B) % 2**32
        i = (i + 1) % (2*rounds + 2)
        j = (j + 1) % len(word_key)
    
    return key_list