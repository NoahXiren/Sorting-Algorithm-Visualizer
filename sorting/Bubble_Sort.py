from scripts.utilis import Draw_list
from scripts.Constants import *
def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2  = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                Draw_list(draw_info, {j: COLOR["green"], j+1: COLOR["red"]}, True)
                yield True
    return lst