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