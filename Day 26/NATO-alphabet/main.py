
import pandas

#TODO 1. Create a dictionary in this format:

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_df.to_dict())

data = {row.letter:row.code for (index,row) in nato_df.iterrows()}
print(data)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    word = str(input("Enter Word:")).upper()
    try:
        split = [data[l] for l in word]
    except:
        print("Sorry, only letters in alphabet please")
    else:
        print(split)



