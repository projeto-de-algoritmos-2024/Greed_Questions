from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time = 0
        result = 0
        for duration, deadline in courses:
            time += duration
            result += 1
            if deadline < time:
                result -= 1
                return result