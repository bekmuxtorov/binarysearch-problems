# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:48:24 2022

@author: Asadbek Muxtorov

@problem: You are given a list of integers rooms and an 
integer target. Return the first integer in rooms that's 
target or larger. If there is no solution, return -1.

@link: https://binarysearch.com/problems/First-Fit-Room

"""
def solve(rooms: list[int], target: int) -> int:
    for room in rooms:
        if room >= target:
            return room
        
    return -1
            

rooms = [20]
target = 20
print(solve(rooms, target))