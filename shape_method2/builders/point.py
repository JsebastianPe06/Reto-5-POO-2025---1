from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

    def compute_distance(self, point)->float:
        return sqrt(((self.x-point.x)**2)+((self.y-point.y)**2))
    
    def __str__(self):
        return f"[{self.x}, {self.y}]"