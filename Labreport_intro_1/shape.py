from math import pi

h = 5.0 # height
r = 1.5 # radius
if __name__ == '__main__':
    area_parallelogram = h * r
    print('The area of the parallelogram is %.3f' % area_parallelogram)
    area_square = r ** 2
    print('The area of the square is %g' % area_square)
    area_circle = pi * r ** 2
    print('The area of the circle is %.3f' % area_circle)
    volume_cone = 1.0 / 3 * pi * r ** 2 * h
    print('The volume of the cone is %.3f' % volume_cone)