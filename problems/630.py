from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        day = 0
        for duration, deadline in courses:
            day += duration
            heapq.heappush(heap, -duration)
            if day > deadline:
                day += heapq.heappop(heap)
        return len(heap)
