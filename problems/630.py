from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        day = 0
        start_and_finish = []
        for duration, deadline in courses:
            start_and_finish.append([day, day+duration])
            day += duration
            if day > deadline:
                day -= duration
                start_and_finish.pop()
                break
        return len(start_and_finish)