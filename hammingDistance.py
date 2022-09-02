"""
@user: Asadbek Muxtorov
Hamming Distance

@problem: Given two integers x, and y return the number of positions where their values differ in their binary representations as a 32-bit integer

@link: https://binarysearch.com/problems/Hamming-Distance

"""

def solve(x: int,y: int) -> int:
    return bin(x^y).count('1')

x = 9
y = 5
print(solve(x, y))