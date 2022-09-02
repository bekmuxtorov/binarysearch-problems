# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:00:57 2022

@author: Asadbek Muxtorov

@problem: Given a non-negative integer num, return whether 
it is a palindrome.
Bonus: Can you solve it without using strings?

@link: https://binarysearch.com/problems/Palindromic-Integer

"""
# def solve(num: int) -> bool:
#     num_items = [str(i) for i in str(num)]
#     num_reverse = ''
#     for i in range(len(num_items)):
#         num_reverse += num_items.pop()
        
#     return str(num) == num_reverse

# num = 121211
# print(solve(num))

# not using string

def solve(num: int) -> bool:
    if num == 0: return True
    
    num_reverse = 0
    num_copy = num
    while num > 0:
        num_reverse = (10 * num_reverse) + num % 10
        num = num // 10
        
    return num_copy == num_reverse

num = 121
print(solve(num))















