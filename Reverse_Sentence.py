def reverse_words_order_and_swap_cases(sentence):
    word_list = sentence.split()
    print(word_list)
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()
print(reverse_words_order_and_swap_cases("Ashok kumar"))