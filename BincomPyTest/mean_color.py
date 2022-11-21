import random
import math

def get_mean(array):
    num = 0

    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    for i in array:
        num += i
    result= math.ceil(num / len(array))
    if(result == Yellow):
        return "Yellow"
    if(result == Green):
        return "Green"
    if(result == Brown):
        return "Brown"
    if(result == Blue):
        return "Blue"
    if(result == Orange):
        return "Orange and Red"
    if(result == White):
        return "White"
    if(result == Cream):
        return "Cream"
    if(result == Arsh):
        return "Arsh"
    if(result == Black):
        return "Black"
    if(result == Pink):
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

print("mean color worn: ", get_mean(color_array))