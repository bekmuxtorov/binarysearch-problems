"""
@user: Asadbek Muxtorov
Clock Angle

@problem: Given a clock time with hour and integer minutes, determine the smaller angle between the hour and the minute hands and floor it to the nearest integer.
Note that the hour hand moves too.
Bonus: When, during the course of a day, will the angle be zero?

@link: https://binarysearch.com/problems/Clock-Angle

"""
import math
def solve(hour: int, minutes):
    delta_hour = 12 - hour
    burchak = abs(minutes * 6 + 30 * delta_hour - 0.5 * minutes)
    return min(burchak, 360 - burchak)


hour = 19
minutes = 53
print(solve(hour, minutes))
