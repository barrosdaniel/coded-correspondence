alphabet = "abcdefghijklmnopqrstuvwxyz"
special_characters = "`~!@#$%^&*()_+-=[]|;':,./<>? "

print("Vigenere Cipher Decrypter")
print("Enter the encrypted message:")
message = input("> ")
# message = "barry is the spy"
print("Enter the keyword:")
keyword = input("> ")
# keyword = "dog"

def create_keyword_phrase(message, keyword):
    keyword_phrase = ""
    index = 0
    for letter in message:
        if letter in special_characters:
            keyword_phrase += letter
        else:
            keyword_phrase += keyword[index]
            index = (index + 1) % len(keyword)
    return keyword_phrase

def get_result_place_value(letter, key_letter):
    place_value = -1
    index_letter = alphabet.find(letter)
    index_key_letter = alphabet.find(key_letter)
    place_value = (index_letter - index_key_letter) % len(alphabet)
    return place_value

def create_resulting_place_value(message, keyword):
    resulting_place_value = []
    keyword_phrase = create_keyword_phrase(message, keyword)
    for i in range(len(message)):
        if message[i] in special_characters:
            resulting_place_value.append(message[i])
        else:
            place_value = get_result_place_value(message[i], keyword_phrase[i])
            resulting_place_value.append(place_value)
    return resulting_place_value

def encrypt(message, keyword):
    encrypted_message = ""
    resulting_place_value = create_resulting_place_value(message, keyword)
    for i in range(len(message)):
        if message[i] in special_characters:
            encrypted_message += message[i]
        else:
            encrypted_message += alphabet[resulting_place_value[i]]
    return encrypted_message

print(encrypt(message, keyword))