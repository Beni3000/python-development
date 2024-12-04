# 1 задание
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common = list(set1.intersection(set2))

    return common

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = common_elements(list_a, list_b)
print(result)

# 2 задание

def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    unique_list = (set1 - set2) | (set2 - set1)

    return list(unique_list)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = unique_elements(list1, list2)
print(result)

# 3 задание

def to_lowercase(input_string):
    return input_string.lower()

result = to_lowercase('Всем привет')
print(result)

# 4 задание

def join_strings_with_separator(string_list):
    return '---'.join(string_list)

result = join_strings_with_separator(['a', 'b', 'c'])
print(result)
