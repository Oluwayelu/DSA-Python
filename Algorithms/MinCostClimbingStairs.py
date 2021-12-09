# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:52:24 2021

@author: U

Question: You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Constraints:

    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
     

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

from jovian.pythondsa import evaluate_test_cases

tests = [
    {
        'input': {
            'cost': [10, 15, 20]
        },
        'output': 15
    },
    {
        'input': {
            'cost': [1,100,1,1,1,100,1,1,100,1]
        },
        'output': 6
    },
 ]

def minCostClimbingStairs(cost):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i -1], dp[i-2])
        
    return min(dp[-2:])

evaluate_test_cases(minCostClimbingStairs, tests)