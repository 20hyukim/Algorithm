def find_max(num_list):
    max_num = max(num_list)
    max_index = num_list.index(max_num)
    print(max_num)
    print(max_index + 1)
    return


def make_array():
    num_list = []
    for i in range(9):
        num_list.append(int(input()))

    return num_list


find_max(make_array())