"""
@user: Asadbek Muxtorov
Integer to Base 3

@problem: Given an integer n, return its base 3 representation as a string.

@link: https://binarysearch.com/problems/Integer-to-Base-3

"""
def solve(num: int) -> str:
    result = ''
    if num == 0:
        return '0'
    
    while num > 0:
        result += str(num % 3)
        num = num // 3
    return result[::-1]

num = 11
print(solve(num))