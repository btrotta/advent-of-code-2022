import numpy as np
from utilities import parse_multi_string, show_image

arr = parse_multi_string()


def draw_pixel(cursor_ind, X, display):
    cursor_row = cursor_ind // 40
    cursor_col = cursor_ind % 40
    if abs(cursor_col - X) <= 1:
        display[cursor_row, cursor_col] = 1
    return cursor_ind + 1


X = 1
display = np.zeros((6, 40))
cursor_ind = 0
for i, a in enumerate(arr):
    if a[0] == "noop":
        cursor_ind = draw_pixel(cursor_ind, X, display)
    else:
        cursor_ind = draw_pixel(cursor_ind, X, display)
        cursor_ind = draw_pixel(cursor_ind, X, display)
        X += int(a[1])

show_image(display)
