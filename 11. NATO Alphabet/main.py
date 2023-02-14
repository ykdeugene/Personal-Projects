import pandas

# with open('nato_phonetic_alphabet.csv') as nato_phonetic_alphabet:
#     data = nato_phonetic_alphabet.readlines()
#
# dictionary = {data[x].split(',')[0]:data[x].split(',')[1].strip() for x in range(1, 27)}
#
# name = input("What is your name?").upper()
# output = [dictionary[alphabet] for alphabet in name]
# print(output)

data = pandas.read_csv('nato_phonetic_alphabet.csv')

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    name = input("What is your name?").upper()
    try:
        output = [dictionary[alphabet] for alphabet in name]
    except KeyError:
        print("You have input an incorrect entry.")
    else:
        print(output)