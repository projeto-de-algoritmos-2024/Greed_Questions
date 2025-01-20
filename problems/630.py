# Course Schedule III
# Url: https://leetcode.com/problems/course-schedule-iii/
# Difficulty: Hard
# Description: 
    # There are n different online courses numbered from 1 to n. 
    # You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith 
    # course should be taken continuously for durationi days and must be finished before or on lastDayi.
    # You will start on the 1st day and you cannot take two or more courses simultaneously.
    # Return the maximum number of courses that you can take.
# Example:
    # Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    # Output: 3

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
