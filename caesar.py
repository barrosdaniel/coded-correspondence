message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

alphabet = "abcdefghijklmnopqrstuvwxyz"
special_characters = "`~!@#$%^&*()_+-=[]|;':,./<>? "

def create_decrypt_alphabet(alphabet, offset):
    encrypt_alphabet = ""
    for letter in alphabet:
        index = (alphabet.find(letter) - offset) % len(alphabet)
        encrypt_alphabet += alphabet[index]
    return encrypt_alphabet

def create_encrypt_alphabet(alphabet, offset):
    decrypt_alphabet = ""
    for letter in alphabet:
        index = (alphabet.find(letter) + offset) % len(alphabet)
        decrypt_alphabet += alphabet[index]
    return decrypt_alphabet

def decrypt(message, offset):
    decrypted_message = ""
    decrypt_alphabet = create_decrypt_alphabet(alphabet, offset)
    for letter in message:
        if letter in special_characters:
            decrypted_message += letter
        else:
            letter_index = decrypt_alphabet.find(letter)
            decrypted_message += alphabet[letter_index]
    return decrypted_message

print(decrypt(message, 10))
message = "My name is Daniel and I love Python!"

def encrypt(message, offset):
    message = message.lower()
    encrypted_message = ""
    encrypt_alphabet = create_encrypt_alphabet(alphabet, offset)
    for letter in message:
        if letter in special_characters:
            encrypted_message += letter
        else:
            letter_index = encrypt_alphabet.find(letter)
            encrypted_message += alphabet[letter_index]
    return encrypted_message

print(encrypt(message, 10))
print(decrypt(encrypt(message, 10), 10))

message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decrypt(message, 10))

message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(decrypt(message, 14))

# Brute force
message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(26):
    print(decrypt(message, i))