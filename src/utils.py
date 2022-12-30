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

def dec_to_base64(dec):
    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    return base64[dec]

def int_arr_to_base64(int_arr):
    base64 = ''
    for i in int_arr:
        base64 += dec_to_base64(i)
    return base64
