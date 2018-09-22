text = "This is only a test. A test of the Emergency Broadcast System."
print("Original:  ", text)


# convert to utf-8 and add '1'
def encrypt(plain_text):
    encrypted_text = ""
    for c in plain_text:
        x = ord(c)
        x += 1
        c2 = chr(x)
        encrypted_text += c2
    return (encrypted_text)


# take string and subtract "1" from utf-8
def decrypt(encrypted_text):
    plain_text_2 = ""
    for d in encrypted_text:
        y = ord(d)
        y -= 1
        d2 = chr(y)
        plain_text_2 += d2
    return (plain_text_2)


a = encrypt(text)
print("Encrypted: ", a)

b = decrypt(a)
print("Decrypted: ", b)
