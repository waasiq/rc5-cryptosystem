import rc5
import keysched
import utils

#* This folder contains code for encryption of cipher text using RC5 algorithm

if __name__ == "__main__":
    text = input('Please enter the text to be encrypted: ')
    key = input('Please enter the key: ')

    # rounds = int(input('Please enter the number of rounds: '))

    # if (round < 0 or rounds > 255):
    #     print('Please enter a valid number of rounds')
    #     exit()

    key_list = keysched.rc5_key_schedule(key, 12)
    cipher_text = rc5.encrypt(text, key_list, 12)
    decoded_text = rc5.decrypt(cipher_text, key_list, 12)
    print('The cipher text is: ', cipher_text)
    print('The decoded text is: ', decoded_text)
    #print(C.decode())
    # bin_text = utils.text_to_binary(text)
    # A,B = rc5.encrypt(bin_text, key_list, 12)
    