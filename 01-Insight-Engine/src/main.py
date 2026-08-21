# check requirement.txt for the challenge instruction

print("=" * 40)
print("\tINSIGHT ENGINE")
print("=" * 40)


while True:

    user_input = input("Enter a piece of text:\n")
    texts = user_input.split()
    if texts:
            
        # Calculate the total number of characters across all words.
        # This is used to calculate the average word length.
        total_word_characters = 0
        for word in texts:
            total_word_characters = total_word_characters + len(word)

        # loops through each word to find the Longest word then stores the length in longest_word_checker.
        longest_word_length = 0 
        longest_word = ""
        for word in texts:
            if len(word) > longest_word_length:
                longest_word_length = len(word)
                longest_word = word
        # print(f"The longest word is: {the_longest_word} with Length:{longest_word_checker}")
        
        print("-" * 15,"INSIGHTS","-" * 15)
        print(f"Characters: {len(user_input)}")
        print(f"Words:\t{len(texts)}")
        print(f"Longest Word: {longest_word}")
        print(f"Average word Length: {total_word_characters/len(texts): .1f}")


        break
    if not texts:
        print("Oops! invalid Input")
        continue



