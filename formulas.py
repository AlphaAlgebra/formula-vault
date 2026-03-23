
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
