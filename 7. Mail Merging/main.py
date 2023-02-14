# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# gets total names in txt file and put into a list
with open(r'C:\Users\ykdeu\PycharmProjects\Day 24-2 Mail Merging\Input\Names\invited_names.txt',
          mode='r') as invited_names:
    file_string = invited_names.read()
    name_list = file_string.split('\n')

with open(r'C:\Users\ykdeu\PycharmProjects\Day 24-2 Mail Merging\Input\Letters\starting_letter.txt',
          mode='r') as starting_letter:
    letter_template = starting_letter.read(-1)
    for name in name_list:
        letter = letter_template.replace("[name]", name)
        with open(rf'C:\Users\ykdeu\PycharmProjects\Day 24-2 Mail Merging\Output\ReadyToSend\letter_for_{name}.txt',
             mode='w') as letter_for:
            letter_for.write(letter)
