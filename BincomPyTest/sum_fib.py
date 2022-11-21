def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result


numFibValues = 50

i = 1
fib_sequence = []

while i <= numFibValues:
    fibValue = fib(i)
    fib_sequence.append(fibValue)
    print(fibValue)
    i += 1
print("All done!")

fib_sum = 0
for i in fib_sequence:
    fib_sum += i
print("Total Fib Sequence: ", fib_sum)
