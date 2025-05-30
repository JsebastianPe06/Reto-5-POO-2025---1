from typing import List

from shape_method2.builders.point import Point
from shape_method2.figures.triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(False, vertices)
        com = super().classify_triangle()
        if(com[0] != "TriRectangle"):
            super().__init__(False, [])