def calculate_slope(x1, y1, x2, y2):
    """Calculates the slope (m) between two points."""
    try:
        m = (y2 - y1) / (x2 - x1)
        return m
    except ZeroDivisionError:
        return "Undefined (Vertical Line)"
