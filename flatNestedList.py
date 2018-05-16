#!usr/bin/python


flat_list = list()


def flatten_nested_lists(nested_list):

    for i in nested_list:
        if type(i) == int:
            flat_list.append(i)
        else:
            flatten_nested_lists(i)

    return flat_list




list_ex = [[1, 2], 3, [4, 5, [6]], [[[[90]]]]]
# list_ex = [1, [4, [6]]]
print(flatten_nested_lists(list_ex))
