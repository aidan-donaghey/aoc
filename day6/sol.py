file_path = "data.prod"


def get_input_string(file_path: str) -> str:
    with open(file_path) as fp:
        return fp.read()


def get_sol(input_string: str, window_size: int) -> int:
    for index, char in enumerate(input_string[:-window_size]):
        if input_string[index:index + window_size] == ''.join(
                dict.fromkeys(input_string[index:index + window_size]).keys()):
            return index + window_size


def main():
    input_string = get_input_string(file_path)
    print(get_sol(input_string, 4))
    print(get_sol(input_string, 14))


if __name__ == "__main__":
    main()
