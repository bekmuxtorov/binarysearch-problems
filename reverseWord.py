
"""
@user: Asadbek Muxtorov
Reverse Word

@problem: Given a string s of words delimited by spaces, reverse the order of words.

@link: https://binarysearch.com/problems/Reverse-Words

@status: easy

"""

# def reverse_word(sentence: str) -> str:
#     word_items = sentence.split(' ')
#     new_word = ''
#     for i in range(len(word_items)):
#         if i != 0:
#             new_word += f" {word_items.pop()}"
#         else:
#             new_word += f"{word_items.pop()}"


#     return new_word

def reverse_word(sentence: str):
    s = sentence.split(' ')
    s = s[::-1]
    return " ".join(s)


sentence = "Asadbek Muxtorov"
print(reverse_word(sentence))