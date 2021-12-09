# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:47:57 2021

@author: Oluwayelu Ifeoluwa David

Question: You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Constraints:
    
    1 <= n <= 45

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

from jovian.pythondsa import evaluate_test_cases

tests = [
    {
        'input': {
            'n': 2
        },
        'output': 2
    }
 ]

def climbStairs(n):
    if n <= 2: return n
    
    current, prev1, prev2 =  0, 1, 2
    for i in range(2, n):
        current = prev1 + prev2
        prev1, prev2 = prev2, current
        
    return current

evaluate_test_cases(climbStairs, tests)