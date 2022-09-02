# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:23:31 2022

@author: Asadbek Muxtorov

@problem: Given an integer n, return a list of integers from 1 to n as strings
except for multiples of 3 use “Fizz” instead of the integer and for the multiples
of 5 use “Buzz”. For integers which are multiples of both 3 and 5 use “FizzBuzz”.

@link: https://binarysearch.com/problems/FizzBuzz

"""

# def solve(n: int) -> list[str]:
#     nums = list(range(1,n+1))
#     result = []
    
#     for num in nums:
#         if num % 15 == 0:
#             result.append('FizzBuzz')
#         elif num % 5 == 0:
#             result.append('Buzz')
#         elif num % 3 == 0:
#             result.append('Fizz')
#         else:
#             result.append(str(num))
    
#     return result

def solve(n: int) -> list[str]:
    return ['FizzBuzz' if not i % 15 else 'Buzz' if not i % 5 else 'Fizz' if not i % 3  else str(i)  for i in range(1, n+1)]
n = 15
print(solve(n))
