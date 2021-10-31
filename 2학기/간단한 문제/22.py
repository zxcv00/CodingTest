def pickup_even(items):
    result = []

    for i in items:
        if i % 2 == 0:
            result.append(i)

    return result



print(pickup_even([3, 4, 5, 6, 7, 8]))