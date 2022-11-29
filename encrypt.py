import rc5
import keysched

#* This folder contains code for encryption of cipher text using RC5 algorithm

if __name__ == "__main__":
    text = input('Please enter the text to be encrypted: ')
    key = input('Please enter the key: ')

    # rounds = int(input('Please enter the number of rounds: '))

    # if (round < 0 or rounds > 255):
    #     print('Please enter a valid number of rounds')
    #     exit()

    key_list = keysched.main_key_scheduler(key, 12)

    # binary = rc5.text_to_binary(text)
    # binary_list = rc5.divide_into_64_bits(binary)
    # word_list = rc5.divide_into_32_bits(binary_list[0])
    # print(word_list)
    #key_list = keysched.main_key_scheduler(key, 8)

