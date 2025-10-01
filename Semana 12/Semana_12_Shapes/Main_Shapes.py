from Class_Circle import Circle
from Class_Square import Square
from Class_Rectangle import Rectangle


def main():
    shapes = [
        Circle(5),
        Square(4),
        Rectangle(3, 6)
    ]

    for shape in shapes:
        print(f'{shape.__class__,__name__}: '
              f'Perimeter={shape.calculate_perimeter():.2f}, '
              f'Area={shape.calculate_area():.2f}')
        
if __name__ == '__main__':
    main()