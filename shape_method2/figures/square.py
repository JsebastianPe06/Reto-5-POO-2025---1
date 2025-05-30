from typing import List

from shape_method2.builders.point import Point
from shape_method2.figures.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(True, vertices)
