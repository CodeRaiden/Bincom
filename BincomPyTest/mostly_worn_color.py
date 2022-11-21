import random
import math

def get_mostly_worn(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    if(array[0] == Yellow):
        return "Yellow"
    if(array[0] == Green):
        return "Green"
    if(array[0] == Brown):
        return "Brown"
    if(array[0] == Blue):
        return "Blue"
    if(array[0] == Orange):
        return "Orange"
    if(array[0] == Red):
        return "Red"
    if(array[0] == White):
        return "White"
    if(array[0] == Cream):
        return "Cream"
    if(array[0] == Arsh):
        return "Arsh"
    if(array[0] == Black):
        return "Black"
    if(array[0] == Pink):
        return "Pink"


Yellow = 5
Green = 10
Brown = 6
Blue = 31
Orange = 9
Red = 9
White = 16
Cream = 2
Arsh = 1
Black = 1
Pink = 4

color_array = [Yellow, Green, Brown, Blue, Orange, Red, White, Cream, Arsh, Black, Pink]

print("mean num: ", get_mostly_worn(color_array))