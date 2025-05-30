from math import sqrt, atan, acos, degrees
from typing import List

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
    

class Square(Rectangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(True, vertices)

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

class Isosceles(Triangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(False, vertices)
        com = super().classify_triangle()
        if(com[-1] != "Isosceles"):
            super().__init__(False, [])

class Equilateral(Triangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(True, vertices)
        com = super().classify_triangle()
        if(com[-1] != "Equilateral"):
            super().__init__(True, [])

class TriRectangle(Triangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(False, vertices)
        com = super().classify_triangle()
        if(com[0] != "TriRectangle"):
            super().__init__(False, [])

class Scalene(Triangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(False, vertices)
        com = super().classify_triangle()
        if(com[-1] != "Scalene"):
            super().__init__(False, [])