"""
@user: Asadbek Muxtorov
Remove one Letter

@problem: Given two strings s0 and s1, return whether you can obtain s1 by removing 1 letter from s0.changed.

@link: https://binarysearch.com/problems/Remove-One-Letter

@status: easy

"""
def solve(s0: str, s1: str) -> bool:
    m, n = len(s0), len(s1)
    
    if m != n+1:
        return False
    
    j = 0
    for i in range(len(s0)):
        if j == n:
            return True
        
        if s0[i] == s1[j]:
            j += 1

    return j == n

            



s0 = "hlo"
s1 = "helo"
print(solve(s0,s1))