alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
for letter in message :
    if letter in alphabet :
        index = alphabet.find(letter)
        if (index + 10) >= len(alphabet) :
            new_index = (index+10) - len(alphabet) 
            new_letter = alphabet[new_index]
            translated_message += new_letter
        else :
            new_letter = alphabet[index+10]
            translated_message += new_letter
    else :
        translated_message += letter

print(translated_message)


def caesar_cipher_maker(text) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_fixed = text.lower()
    translated_message = ""
    for letter in text_fixed :
        if letter in alphabet :
            index = alphabet.find(letter)
            if index + 10 >= 26 :
                new_index = (index + 10) - len(alphabet)
                translated_message += alphabet[new_index]
            else :
                translated_message += alphabet[index+10]
        else :
            translated_message += letter
    
    return translated_message

print(caesar_cipher_maker("Hello World"))
