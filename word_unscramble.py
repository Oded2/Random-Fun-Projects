from word_lists import word_list_lower
word_list = []
common_list = []
counted_letters = []
user_input = input('Put in your letters ').lower()
user_letters = list(user_input)
for letter in user_letters:
    counting_letters = (user_letters.count(letter))
    counted_letters.append(counting_letters)
print(counted_letters)

confirmation = 'oded is cool'
while confirmation[0] != 'y' and confirmation[0] != 'n':
    confirmation = input('Would you like for the words to have the same length as your word? (Yes/No). ').lower()
if confirmation[0] == 'n':
    for i in word_list_lower:
        word_letters = list(i)
        common_list = []
        for common in word_letters:
            if common in user_letters:
                common_list.append(common)
        if common_list == word_letters:
            word_list.append(i)



    print(common_list)
    print(word_list)
    for m in word_list:
        print(m)
    print(f'There are {len(word_list):,} words that have the same letters the word "{user_input}"')
else:
    for i in word_list_lower:
        common_list = set(list(i)).intersection(user_letters)
        if len(common_list) == len(user_input) == len(i):
            word_list.append(i)
        print(f'There are no words that have the same letters as the word "{user_input}')
    else:
        for r in word_list:
            print(r)
        print(f'There are {len(word_list):,} words that have the same letters the word "{user_input}"')
# sort them by the amount of letters they are
# cant use the same letter twice eg: raawd cannot display radar