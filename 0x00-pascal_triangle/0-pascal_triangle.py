#!/usr/bin/python3
"""This function is used to generate the output of the pascal triangle."""


def pascal_triangle(n):
    """Generate the pascal triangle from the given number of points."""
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    last_triangle = pascal_triangle(n - 1)
    triangle = last_triangle
    new_triangle = [1]
    for i in range(1, len(last_triangle[-1])):
        new_triangle.append(last_triangle[-1][i-1] + last_triangle[-1][i])
    new_triangle.append(1)
    triangle.append(new_triangle)
    return triangle
