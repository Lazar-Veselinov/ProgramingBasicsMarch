num_one = int(input())
num_two = int(input())

for num in range(num_one, num_two + 1):

    sum_even = 0
    sum_odd = 0

    for index, digit in enumerate(str(num)):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(num, end = " ")