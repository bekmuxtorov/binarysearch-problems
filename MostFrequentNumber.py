"""
Created on Wed Jul 13 12:07:46 2022

@author: Asadbek Muxtorov

@problem: You are given a list of list of integers intervals where each 
element contains the inclusive interval [start, end].
Return the most frequently occurring number in the intervals.
If there are ties, return the smallest number.

@link: https://binarysearch.com/problems/Most-Frequent-Number-in-Intervals

"""

def solve(intervals: list[int]) -> int:
    a_sonlar = []
    for interval in intervals:
       a_sonlar =  a_sonlar + list(range(interval[0],interval[1]))
        
    return a_sonlar        

intervals = [
    [1, 4],
    [3, 5],
    [6, 9],
    [7, 9]
]
print(solve(intervals))

