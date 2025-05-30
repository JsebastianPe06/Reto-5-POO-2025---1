from shape_method1.class_shape.shape1 import Point as PointMethod1
from shape_method1.class_shape.shape1 import Rectangle as RectangleMethod1
from shape_method1.class_shape.shape1 import Isosceles as IsoscelesMethod1
from shape_method1.class_shape.shape1 import TriRectangle as TriRectangleMethod1

from shape_method2.builders.point import Point as PointMethod2
from shape_method2.figures.rectangle import Rectangle as RectangleMethod2
from shape_method2.figures.triangles.isosceles import Isosceles as IsoscelesMethod2
from shape_method2.figures.triangles.trirectangle import TriRectangle as TriRectangleMethod2

point1 = PointMethod1()
point2 = PointMethod1(2,0)
point3 = PointMethod1(2,4)
point4 = PointMethod1(0,4)
point5 = PointMethod1(1,0)
point6 = PointMethod1(2,1)
point7 = PointMethod1(2,6)
point8 = PointMethod1(0,1)
point9 = PointMethod1(2,2)
point10 = PointMethod2()
point11 = PointMethod2(2,0)
point12 = PointMethod2(2,4)
point13 = PointMethod2(0,4)
point14 = PointMethod2(1,0)
point15 = PointMethod2(2,1)
point16 = PointMethod2(2,6)
point17 = PointMethod2(0,1)
point18 = PointMethod2(2,2)
vertices1 = [point1, point2, point3, point4]
vertices2 = [point5, point6, point7, point8]
vertices3 = [point1, point2, point4]
vertices4 = [point1, point4, point9]
vertices5 = [point10, point11, point12, point13]
vertices6 = [point14, point15, point16, point17]
vertices7 = [point10, point11, point13]
vertices8 = [point10, point13, point18]

if __name__ == "__main__":
    print("\n### METHOD 1 ###")
    #test 1
    rectangle1 = RectangleMethod1(False, vertices1)
    print(rectangle1)
    rectangle1.set_vertices(vertices2)
    print(rectangle1)
    #Test 2
    triangle1 = TriRectangleMethod1(vertices3)
    print(triangle1)
    #Test 3
    triangle2 = TriRectangleMethod1(vertices4)
    print(triangle2)
    print(triangle2.get_inner_angles())
    #Test 4
    triangle3 = IsoscelesMethod1(vertices4)
    print(triangle3)

    print("\n### METHOD 2 ###")
    #test 1
    rectangle2 = RectangleMethod2(False, vertices1)
    print(rectangle2)
    rectangle2.set_vertices(vertices2)
    print(rectangle2)
    #Test 2
    triangle4 = TriRectangleMethod2(vertices7)
    print(triangle4)
    #Test 3
    triangle5 = TriRectangleMethod2(vertices8)
    print(triangle5)
    print(triangle5.get_inner_angles())
    #Test 4
    triangle6 = IsoscelesMethod2(vertices8)
    print(triangle6)