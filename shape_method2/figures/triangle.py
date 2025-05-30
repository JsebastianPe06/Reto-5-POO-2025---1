from math import sqrt
from typing import List

from shape_method2.builders.point import Point
from shape_method2.builders.shape2 import Shape

class Triangle(Shape):
    def __init__(self, is_regular:bool, vertices:List[Point]):
        super().__init__(is_regular, 3)
        super().set_vertices(vertices)

    def classify_triangle(self)->str:
        margin_error = 1e-6
        com = []
        if(len(self._edges) != 0):
            if(sum(abs(90-i) < margin_error for i in self._inner_angles) == 1):
                com.append("TriRectangle")
            if(all(abs(i.length-self._edges[0].length) < margin_error for i in self._edges)):
                com.append("Equilateral")
                return com
            elif(all(abs(i.length - self._edges[0].length) > margin_error for i in self._edges)
            and abs(self._edges[1].length - self._edges[2].length) > margin_error):
                com.append("Scalene")
                return com
            com.append("Isosceles")
            return com
        return None

    def compute_perimeter(self):
        if(len(self._edges) != 0):
            return sum(i.length for i in self._edges)
        return None
    
    def compute_area(self):
        if(len(self._edges) != 0):
            s = sum(i.length for i in self._edges)/2
            a, b, c = (i.length for i in self._edges)
            return sqrt(s*(s-a)*(s-b)*(s-c))