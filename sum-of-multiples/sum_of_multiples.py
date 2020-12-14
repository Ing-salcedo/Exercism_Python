def sum_of_multiples(limit, multiples):
    sum = 0
    lowest_multiply = sorted(multiples)[0] if len(multiples) != 0 else 0

    for i in range(lowest_multiply, limit):
        for j in multiples:
            if j != 0 and i % j == 0:
                sum += i
                break

    return sum
