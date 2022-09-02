
"""
@user: Asadbek Muxtorov
Is Anogram

@problem: Given two strings s0 and s1, return whether they are anagrams of each other.

@link: https://binarysearch.com/problems/Anagram-Checks

@status: easy

"""
def isAnogram(s0: str, s1: str) -> bool:
    s0_items = [str(i) for i in s0]
    s1_items = [str(i) for i in s1]
    s0_item_count = {}
    for s0_item in s0_items:
        s0_item_count[s0_item] = s0_items.count(s0_item)

    s1_item_count = {}
    for s1_item in s1_items:
        s1_item_count[s1_item] = s1_items.count(s1_item)


    return s0_item_count == s1_item_count


s0 = 'sadf'
s1 = 'silent'

print(isAnogram(s0, s1))

# class Solution:
#     def tartibla(self, s: int):
#         return set([str(i) for i in s])
#
#     def solve(self, s0, s1):
#         return self.tartibla(s0) == self.tartibla(s1) and len(s0) == len(s1)
#
