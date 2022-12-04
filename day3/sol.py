file_path = "data.prod"


def convert_to_priority(char: str):
    return ord(char) - 96 if char.islower() else ord(char) - 38


def find_error(*args):
    current_set = {convert_to_priority(i) for i in args[0]}
    for x in args[1:]:
        new_set = {convert_to_priority(i) for i in x}
        current_set.intersection_update(new_set)
    return current_set.pop()


# with open(file_path) as fp:
#     error_priority_list = []
#     for line in fp:
#         line = line.strip()
#
#         error_priority_list.append(find_error(first_half, second_half))
#     print(sum(error_priority_list))

with open(file_path) as fp:
    data = [line.strip() for line in fp]

# Sol 1
error_priority_list = []
for line in data:
    first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
    error_priority_list.append(find_error(first_half, second_half))
# print(sum(error_priority_list))

# Sol 2
big_list = []
error_priority_list = []
d = []
for count, line in enumerate(data):
    if count % 3 == 0:
        d.append(line)
    elif count % 3 == 1:
        d.append(line)
    else:
        d.append(line)
        big_list.append(d)
        d = []

for line in big_list:
    error_priority_list.append(find_error(*line))
print(sum(error_priority_list))
