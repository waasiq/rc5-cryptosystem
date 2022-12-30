import rc5
import keysched
import base64

#* This folder contains code for encryption of cipher text using RC5 algorithm

def bytes_to_base64(b):
    return base64.b64encode(b).decode()

def base64_to_bytes(b):
    return base64.b64decode(b)

if __name__ == "__main__":
    choice = input('Please enter 1 for encryption and 2 for decryption and 3 to quit: ')
    while (choice != '3'):
        if (choice == '1'):
            text = input('Please enter the text to be encrypted: ')
            key = input('Please enter the key: ')
            rounds = int(input('Please enter the number of rounds: '))

            if (rounds < 0 or rounds > 255):
                print('Please enter a valid number of rounds')
                exit()

            key_list = keysched.rc5_key_schedule(key, rounds)
            cipher_text = rc5.encrypt(text, key_list, rounds)
        
            print('Encrypted text: ' ,bytes_to_base64(cipher_text))
        elif (choice == '2'):
            cipher_text = base64_to_bytes(input('Please enter the cipher text to be decrypted: '))
            key = input('Please enter the key: ')
            rounds = int(input('Please enter the number of rounds: '))

            if (rounds < 0 or rounds > 255):
                print('Please enter a valid number of rounds')
                exit()

            key_list = keysched.rc5_key_schedule(key, rounds)
            decoded_text = rc5.decrypt(cipher_text, key_list, rounds)
            print('Decrypted text: ' ,decoded_text)
        
        choice = input('Please enter 1 for encryption and 2 for decryption and 3 to quit: ')
    
    