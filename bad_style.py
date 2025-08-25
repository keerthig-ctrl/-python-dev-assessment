def calculate_area(length, width):
    """Return the rectangle area;print a note if it's large"""
    result = length * width
    if result > 100:
        print("Large area!")
    return result


def main():
    my_length = 10
    my_width = 5
    area = calculate_area(my_length, my_width)
    print(f"The area is:", (area))
