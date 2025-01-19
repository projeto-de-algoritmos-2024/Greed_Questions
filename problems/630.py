from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        time = 0
        start_and_finish = []
        for duration, deadline in courses:
            time += duration
            start_and_finish.append([time, time+duration])
            if time > deadline:
                time -= duration
                start_and_finish.pop()
        return len(start_and_finish)