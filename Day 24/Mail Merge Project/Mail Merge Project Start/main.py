PLACEHOLDER = "[name]"
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()

#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as change:
    letters = change.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
#Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/birthday_for{stripped_name}.txt", mode="w") as add_data:
            add_data.write(new_letter)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp