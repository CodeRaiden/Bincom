import math
import random

# binary numbers

def base_ten(bi_num):
    str(bi_num)
    num = 3
    num_array = []
    add_num = 0

    for i in bi_num:
        n = (int(i) * (2 ** num))
        num_array.append(n)
        num -= 1

    for j in num_array:
        add_num += j

    return add_num


# Generate 4 digit num
four_digit = []
four_digit.append(1)
for i in range(3):
    randNum = random.randint(0, 1)
    four_digit.append(randNum)

bi_num = ""

for j in four_digit:
    bi_num += str(j)

print("generated binary number ", bi_num)
print("converting to base 10... ", base_ten(bi_num))