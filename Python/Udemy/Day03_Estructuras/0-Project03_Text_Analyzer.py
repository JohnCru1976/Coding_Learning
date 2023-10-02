# ****************************************************
# File: 0-Project03_Text_Analyzer.py
# Description: Educational purpose project. The user
#              introduce a text, and then the program
#              analyzes some parameters.
# Date creation: 2023-09-24
# Last update: 2023-09-24
# Author: Juan B. Cru
# ****************************************************

print("Bienvenido a TEXT ANALYZER")
original_text = input("Ingresa cualquier texto: ")
text = original_text.lower()
letter_list = [input("Ingresa la primera letra: ").lower(),
               input("Ingresa la segunda letra: ").lower(),
               input("Ingresa la tercera letra: ").lower()]

# How many times appear the selected letters
print(f"\nLa letra \"{letter_list[0].upper()}\" aparece {text.count(letter_list[0])} veces")
print(f"La letra \"{letter_list[1].upper()}\" aparece {text.count(letter_list[1])} veces")
print(f"La letra \"{letter_list[2].upper()}\" aparece {text.count(letter_list[2])} veces")

# How many words the text has
print(f"\nEl texto tiene {len(text.split())} palabras")

# First and last letter in text
print(f"\nLa primera letra del texto es \"{text[0].upper()}\"")
print(f"La última letra del texto es \"{text[-1].upper()}\"")

# Reverse text
reverse_text_list = original_text.split()
reverse_text_list.reverse()
print(f"\nÉste es el texto invertido: {' '.join(reverse_text_list)}")

# Is the word "Python" in the text?
result = {
    True: "El texto contiene la palabra \"Python\"",
    False: "El texto no contiene la palabra \"Python\""
}
print(f"\n{result['python' in text]}")
