
def find_longest_word(words):
    longest_word = ""
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
            longest_word = word
    return longest_word





# # words = ["Python", "AI", "engineering", "data"]
# # words= ["cat", "dog", "sun"]
# # print(find_longest_word(words))

# assert find_longest_word(["Python", "AI", "engineering", "data"]) == "engineering"
# assert find_longest_word(["cat", "elephant", "dog"]) == "elephant"
# assert find_longest_word(["cat", "dog", "sun"]) == "cat"

# print("All tests passed!")