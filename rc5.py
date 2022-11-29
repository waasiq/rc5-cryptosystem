

#* This py file contains code for coverting text to binary and vice versa

def encrypt(bin_text, key_list, rounds):
    A = int(bin_text[0:32], 2)
    B = int(bin_text[32:64], 2)

    A = A + key_list[0]
    B = B + key_list[1]

    for i in range(1, rounds+1):
        A = ((A ^ B) << (B % 32)) + key_list[2*i]
        B = ((B ^ A) << (A % 32)) + key_list[2*i + 1]
    
    
    return A, B



def text_to_hex(text):
    hex = ''.join(format(ord(i), '02x') for i in text)
    return hex

def text_to_binary(text):
    binary = ''.join(format(ord(i), '08b') for i in text)
    return binary

def divide_into_64_bits(binary):
    binary_list = []
    for i in range(0, len(binary), 64):
        binary_list.append(binary[i:i+64])
    return binary_list
    
def divide_into_words(binary):
    binary_list = []
    for i in range(0, len(binary), 16):
        binary_list.append(binary[i:i+16])
    return binary_list

def divide_into_1_byte(binary):
    binary_list = []
    for i in range(0, len(binary), 8):
        binary_list.append(binary[i:i+8])
    return binary_list

def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def divide_into_32_bits(binary):
    binary_list = []
    for i in range(0, len(binary), 32):
        binary_list.append(binary[i:i+32])
    return binary_list
