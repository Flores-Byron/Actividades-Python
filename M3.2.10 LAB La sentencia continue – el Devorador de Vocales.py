word_without_vowels = ""

user_word = input(print("Ingresa una palabra: "))# Indicar al usuario que ingrese una palabra
user_word = user_word.upper()# y asignarlo a la variable user_word.


for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)# Imprimir la palabra asignada a word_without_vowels.
