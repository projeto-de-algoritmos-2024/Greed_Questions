# 2406. Divide Intervals Into Minimum Number of Groups
# Url: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# Difficulty: Medium
# Description:
	# You are given a 2D integer array intervals where intervals[i] = [lefti, righti] 
	# represents the inclusive interval [lefti, righti]. 
	# You have to divide the intervals into one or more groups such that each 
	# interval is in exactly one group, and no two intervals that are in the 
	# same group intersect each other.
# Return the minimum number of groups you need to make.
# Two intervals intersect if there is at least one common number between them. 
# For example, the intervals [1, 5] and [5, 8] intersect.
# Example:
	# Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
	# Output: 3

import heapq
from types import List

class Solution:
	def minGroups(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x: x[0])
		heap = []
		for left, right in intervals:
			if not heap:
				heapq.heappush(heap, right)
				continue
			if left > heap[0]:
				heapq.heapreplace(heap, right)
			else:
				heapq.heappush(heap, right)
		return len(heap)