"""
@user: Asadbek Muxtorov
3-6-9

@problem: Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap".
Note: return the number as a string.

@link: https://binarysearch.com/problems/3-6-9

@status: easy

"""
def solve(n: int) -> list:
    a_sonlar = list(range(1,n+1))
    new_nums = []
    for a_son in a_sonlar:
        if a_son % 3 == 0 or str(3) in str(a_son) or str(6) in str(a_son) or str(9) in str(a_son):
            new_nums.append('clap')

        else:
            new_nums.append(str(a_son))

    return new_nums


n=16
print(solve(n))