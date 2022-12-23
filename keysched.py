p = 0xB7E15163  # For 32 bit words
q = 0x9E3779b9  # For 32 bit words

def rc5_key_schedule(key, rounds):
    # Convert the key string to a bytes object
    key_bytes = key.encode()

    # Sub keyschedule intialization according to the paper
    S = [0] * 2*(rounds+1)
    S[0] = p
    for i in range(1, len(S)):
        S[i] = S[i-1] + q

    # Mix the key into the key schedule
    l = len(key_bytes) // 4
    L = [0] * (l+1)
    for i in range(l):
        L[i] = int.from_bytes(key_bytes[4*i:4*(i+1)], 'little')
    L[l] = int.from_bytes(key_bytes[4*l:], 'little')

    A = B = i = j = 0
    v = 3 * max(l, 2*(rounds+1))
    for k in range(v):
        A = S[i] = ((S[i] + A + B) & 0xFFFFFFFF)
        B = L[j] = ((L[j] + A + B) & 0xFFFFFFFF)
        i = (i+1) % (2*(rounds+1))
        j = (j+1) % (l+1)

    return S