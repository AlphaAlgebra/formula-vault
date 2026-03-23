import math

def calculate_slope(x1, y1, x2, y2):
    """Calculates the slope (m) between two points."""
    try:
        m = (y2 - y1) / (x2 - x1)
        return m
    except ZeroDivisionError:
        return "Undefined (Vertical Line)"


def calculate_midpoint(x1, y1, x2, y2):
    """Calculates the midpoint (xm, ym) between two points."""
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    return (xm, ym)


def calculate_distance(x1, y1, x2, y2):
    """Calculates the distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_quadratic(a, b, c):
    """Solves for x in ax^2 + bx + c = 0."""
    import math
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real roots"
    
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return round(x1, 2), round(x2, 2)
