from math import degrees, atan

from shape_method2.builders.point import Point

class Line():
    def __init__(self, point_start:Point, point_end:Point):
        self.point_start = point_start
        self.point_end = point_end
        self.length = self.point_start.compute_distance(self.point_end)
        if((point_start.x-point_end.x)==0):
            self.slope = None
            self.cut_point = None
        elif((point_start.y-point_end.y)==0):
            self.slope = 0
            self.cut_point = point_start.y
        else:
            self.slope = (point_start.y-point_end.y)/(point_start.x-point_end.x)
            self.cut_point = -(point_start.y/self.slope)+point_start.x
    
    def evaluate_value_function(self, x:float, reverse:bool)->float:
        if(reverse==False):
            return (self.slope*x)+self.cut_point if(self.slope!=None) else self.point_start.x
        else:
            if(self.cut_point==None or self.slope==0):
                return None
            return (x-self.cut_point)/self.slope
    
    def compute_length(self)->float:
        return self.length
    
    def compute_slope(self):
        return degrees(atan(self.slope)) if(self.slope!=None) else 90
    
    def compute_horizontal_cross(self)->Point:
        if(self.slope!=0):
            if(self.slope==None):
                return Point(self.point_end.x, 0)
            else:
                return Point(self.evaluate_value_function(0, 1), 0)
        else:
            return None
    
    def compute_vertical_cross(self)->Point:
        if(self.slope!=None):
            if(self.slope==0):
                return Point(0, self.point_end.y)
            else:
                return Point(0, self.evaluate_value_function(0, 0))
        else:
            return None
    
    def __str__(self):
        return f"   {self.point_start}-->{self.point_end}\n"