from typing import List

from shape_method2.builders.point import Point
from shape_method2.figures.triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(True, vertices)
        com = super().classify_triangle()
        if(com[-1] != "Equilateral"):
            super().__init__(True, [])