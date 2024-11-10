"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tereza Trčková
email: terda.trckova@seznam.cz
discord: tereza_trckova
"""
# Registrovaní uživatelé
USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Získání přihlašovacích údajů od uživatele
username = input("username: ")
password = input("password: ")

# Ověření přihlašovacích údajů
if username in USERS and USERS[username] == password:
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-" * 40)
else:
    print("unregistered user, terminating the program..")
    exit()

# Výběr textu k analýze
try:
    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if text_choice < 1 or text_choice > len(TEXTS):
        print("Invalid number, terminating the program..")
        exit()
except ValueError:
    print("Invalid input, terminating the program..")
    exit()

selected_text = TEXTS[text_choice - 1]

# Analýza vybraného textu
words = selected_text.split()
word_count = len(words)
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = []

# Procházení slov a provádění analýzy
for word in words:
    cleaned_word = word.strip(".,:;!?")  # Odstranění interpunkce na začátku a konci
    if cleaned_word.isdigit():
        numeric_strings.append(int(cleaned_word))
    elif cleaned_word.istitle():
        titlecase_words += 1
    elif cleaned_word.isupper() and not any(char.isdigit() for char in cleaned_word):
        uppercase_words += 1
    elif cleaned_word.islower():
        lowercase_words += 1

sum_numbers = sum(numeric_strings)

# Výpis výsledků analýzy
print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")
print("-" * 40)

# Vytvoření sloupcového grafu pro četnost délek slov
graph_data = {}
for word in words:
    cleaned_word = word.strip(".,:;!?")  # Odstranění interpunkce na začátku a konci
    word_length = len(cleaned_word)
    if word_length not in graph_data:
        graph_data[word_length] = 0
    graph_data[word_length] += 1

print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for length, count in sorted(graph_data.items()):
    print(f"{length:>3}|{'*' * count:<13}|{count}")

