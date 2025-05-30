from typing import List

from shape_method2.builders.shape2 import Shape
from shape_method2.builders.point import Point
from shape_method2.builders.line import Line

class Rectangle(Shape):
    def __init__(self, is_regular:bool, vertices:List[Point]):
        super().__init__(is_regular, 4)
        self.set_vertices(vertices)
        if(super().is_rectangle(vertices)):
            self.b_left = Point(min(i.x for i in self._vertices), 
                                min(i.y for i in self._vertices))
            self.t_right = Point(max(i.x for i in self._vertices), 
                                max(i.y for i in self._vertices))
        
    def set_vertices(self, vertices:List[Point]):
        if(super().is_rectangle(vertices)):
            super().set_vertices(vertices)
            self.b_left = Point(min(i.x for i in self._vertices), 
                                min(i.y for i in self._vertices))
            self.t_right = Point(max(i.x for i in self._vertices), 
                                max(i.y for i in self._vertices))
            return self._vertices
        print("\nThe rectangle cannot be formed. It will not be updated.\n")
    
    def compute_area(self)-> float:
        if(len(self._edges) != 0):
            return self._edges[0].length*self._edges[1].length
        return None

    def compute_perimeter(self)-> float:
        if(len(self._edges) != 0):
            return sum(i.length for i in self._edges)
        return None
    
    def compute_interference_point(self,point:Point)->bool:
        if(len(self._edges) != 0):
            val_x:bool = point.x >= self.b_left.x and point.x <= self.b_left.x+self._edges[0].length
            val_y:bool = point.y >= self.b_left.y and point.y <= self.b_left.y+self._edges[1].length
            return val_y and val_x
        return None
    
    def compute_interference_line(self,line:Line)->bool:
        if(len(self._edges) != 0):
            a:bool = self.b_left.y<=line.evaluate_value_function(self.b_left.x,0)<=self.t_right.y
            c:bool = self.b_left.y<=line.evaluate_value_function(self.t_right.x,0)<=self.t_right.y
            if(line.evaluate_value_function(self.t_right.y,1)!=None):
                b:bool = self.b_left.x<=line.evaluate_value_function(self.b_left.y,1)<=self.t_right.x
                d:bool = self.b_left.x<=line.evaluate_value_function(self.t_right.y,1)<=self.t_right.x
                return a or b or c or d
            return a or c
        return None