def mean_num_friends(x):
    sum = 0
    for i in x:
        sum += i
    return sum / len(x)


def median_num_friends(x):
    sorted_list = sorted(x)
    mid = int(len(x) / 2)
    if len(x) % 2 == 0:
        return (sorted_list[mid] + sorted_list[mid + 1]) / 2
    else:
        return sorted_list[mid]


num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))
