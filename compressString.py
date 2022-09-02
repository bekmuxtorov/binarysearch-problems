"""
@user: Asadbek Muxtorov
Compress String

@problem: Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.

@link: https://binarysearch.com/problems/Compress-String

@status: easy

"""
def solve(string: str) -> str:
    string_items = [i for i in string]
    s = ''
    for i in string_items:
        if string_items.count(i) != 1:
            s += i
            string_items.remove(i)

    return  s



s = "aaaaaabbbccccaaaaddf"
print(solve(s))
