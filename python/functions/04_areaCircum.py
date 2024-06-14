import math

class solution:
    def circle(self,r):
        area = math.pi*(r**2)
        circumference= 2*math.pi*r
        return area, circumference

print(solution().circle(3))