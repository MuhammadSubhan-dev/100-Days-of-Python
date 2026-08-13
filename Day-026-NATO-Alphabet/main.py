import pandas as pd

nato_alphabet = pd.read_csv("./nato_phonetic_alphabet.csv")     #Dataframe
phonetic_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}  #Iterate through dataframe with each row and storing at into dictionary

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)