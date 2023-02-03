PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names:
    names_contents = names.readlines()
    print(names_contents)

for name in names_contents:
    stripped_name = name.strip()
    file_name = f"letter_for_{stripped_name}.txt"

    with open("./Input/Letters/starting_letter.txt", "r") as letter:
        letter_contents = letter.read()
        letter_contents = letter_contents.replace(PLACEHOLDER, str(stripped_name))

    with open(f"./Output/ReadyToSend/{file_name}", "w") as file:
        file.write(letter_contents)
