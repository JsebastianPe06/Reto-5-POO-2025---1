from math import acos, degrees
from typing import List

from shape_method2.builders.line import Line
from shape_method2.builders.point import Point

class Shape:
    def __init__(self, is_regular:bool, number_sides:int):
        self.is_regular = is_regular
        self.number_sides = number_sides
        self._vertices = []
    
    def check_regularity_points(self, vertices:List[Point]):
        if(self.is_regular):
            reference = vertices[0].compute_distance(vertices[-1])
            margin_error = 1e-6
            for i in range(len(vertices)-1):
                if(reference-vertices[i].compute_distance(vertices[i+1]) > margin_error):
                    return False
            return True
        return True
    
    def set_vertices(self, vertices:List[Point])->List[Point]:
        if(self.check_regularity_points(vertices) and len(vertices) == self.number_sides):
            self._vertices = vertices
            return self._vertices
        print(
            "It is not possible to form the figure with the given vertices."
            "It will not be updated"
        )
    
    def get_vertices(self):
        return self._vertices
    
    @property
    def _edges(self)->List[Line]:
        _edges = []
        if(len(self._vertices) == self.number_sides):
            for i in range(len(self._vertices)-1):
                t = Line(self._vertices[i], self._vertices[i+1])
                _edges.append(t)
            _edges.append(Line(self._vertices[-1], self._vertices[0]))
        return _edges
    
    def get_edges(self):
        return self._edges
    
    @property
    def _inner_angles(self)->List[float]:
        _inner_angles = []
        if(len(self._vertices) == self.number_sides):
            for i in range(len(self._vertices)):
                ref = self._vertices[i]
                v1 = Line(ref, self._vertices[i-1])
                v2 = Line(ref, self._vertices[(i + 1)%len(self._vertices)])
                dot = (
                    (v1.point_end.x-ref.x)*(v2.point_end.x-ref.x)
                    +(v1.point_end.y-ref.y)*(v2.point_end.y-ref.y)
                    )
                _inner_angles.append(degrees(acos(dot/(v1.length*v2.length))))
        return _inner_angles
    
    def get_inner_angles(self)->List[float]:
        return self._inner_angles
    
    def compute_area(self):
        raise NotImplementedError("Method implemented by subclasses")
    
    def compute_perimeter(self):
        raise NotImplementedError("Method implemented by subclasses")
    
    @staticmethod
    def is_rectangle(vertices:List[Point])->bool:
        if(len(vertices) == 4):
            margin_error = 1e-6
            lade_1 = Line(vertices[0], vertices[1])
            lade_2 = Line(vertices[1], vertices[2])
            lade_3 = Line(vertices[2], vertices[3])
            if(abs(lade_1.length-lade_3.length) < margin_error):
                if(lade_1.slope == 0 and lade_3.slope == 0 and lade_2.slope == None):
                    return True
        return False
    
    def __str__(self):
        t1 = f"{self.__class__.__name__}:\n"
        t2, t3, t4 = "vertices: ", "edges:\n", "Inner_angles: "
        if(len(self._vertices) != 0):
            for i in range(self.number_sides):
                t2 += f"P{i}{self._vertices[i]} "
                t3 += f"{self._edges[i]}"
                t4 += f"A{i}({self._inner_angles[i]}°) "
        else:
            return t1+"The vertices haven't defined correctly"
        t5 = f"Perimeter: {self.compute_perimeter()}\nArea: {self.compute_area()}"
        return f"{t1}{t2}\n{t3}{t4}\n{t5}"