file_path = "data.prod"


def get_fully_encapsulated(line):
    first_range, second_range = line.split(",")
    first_start, first_end = first_range.split("-")
    second_start, second_end = second_range.split("-")
    if (first_start <= second_start and first_end >= second_end) or (
            second_start <= first_start and second_end >= first_end):
        print(f"First_range: {first_range} Second_range: {second_range}")
        return True
    return False


number_of_fully_encapsulated = 0

with open(file_path) as fp:
    for cnt, line in enumerate(fp):
        line = line.strip()
        number_of_fully_encapsulated += 1 if get_fully_encapsulated(line) else 0

print(number_of_fully_encapsulated)
