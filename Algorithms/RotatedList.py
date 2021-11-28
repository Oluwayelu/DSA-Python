# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 20:02:23 2021

@author: Oluwayelu Ifeoluwa
"""
from jovian.pythondsa import evaluate_test_cases

tests = [
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3},
    {'input': {'nums': [4, 5, 6, 7, 8, 1, 2, 3]}, 'output': 5},
    {'input': {'nums': [1, 2, 3, 4, 5]}, 'output': 0},
    {'input': {'nums': [7, 3, 5]}, 'output': 1},
    {'input': {'nums': [2, 3, 4, 6, 8, 9, 1]}, 'output': 6},
    {'input': {'nums': [1, 3, 5, 7, 9, 11, 13]}, 'output': 0},
    {'input': {'nums': []}, 'output': 0},
    {'input': {'nums': [5]}, 'output': 0}
]
 
# Liear search algorithm O(N)
def linear_count_rotations(nums):
    position = 0
    
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        
        position += 1
    return 0

# Binary search algorithm O(logN)
def binary_count_rotations(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        print('lo: ', lo, " hi: ", hi, ' mid: ', mid, ' mid_num: ', nums[mid])
        
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        
        elif  nums[mid] < nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 0
            
# Evaluate test cases for linear search algorithm
evaluate_test_cases(linear_count_rotations, tests)

# Evaluate test cases for binary search algorithm
evaluate_test_cases(binary_count_rotations, tests)
