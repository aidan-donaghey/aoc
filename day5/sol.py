file_path = "data.prod"

NUM_OF_STACKS = 9
MAX_HEIGHT = 8


# NUM_OF_STACKS = 3
# MAX_HEIGHT = 3


def generate_processed_list(line):
    return [line[s] for s in range(1, len(line), 4)]


def create_stack(processed_list):
    list_of_stacks = [[] for _ in range(NUM_OF_STACKS)]
    reverse_list = list(reversed(processed_list))
    for row in reverse_list:
        for index, column in enumerate(row):
            list_of_stacks[index].append(column) if column.isalpha() else None
    return list_of_stacks


def process_instructions(line):
    return [int(s) for s in line.split() if s.isdigit()]


def apply_instruction_1(stack, instruction):
    for number_to_move in range(instruction[0]):
        stack[instruction[2] - 1].append(stack[instruction[1] - 1].pop())
    return stack


def apply_instruction_2(stack, instruction):
    # Index 0 is the amount to move from stack
    # Index 1 is the stack to move from
    # Index 2 is the stack to move to
    amount_to_move = instruction[0]
    stack_to_move_from = instruction[1] - 1
    stack_to_move_to = instruction[2] - 1
    slice_to_move = stack[stack_to_move_from][-amount_to_move:]
    stack[stack_to_move_from] = stack[stack_to_move_from][:-amount_to_move]
    stack[stack_to_move_to] = stack[stack_to_move_to] + slice_to_move
    return stack


def top_of_each_stack(list_of_stack):
    return [stack[-1] for stack in list_of_stack]


def main():
    stack_lines = []
    instructions = []
    with open(file_path) as fp:
        # Per Line
        for cnt, line in enumerate(fp):
            if cnt < MAX_HEIGHT:
                stack_lines.append(generate_processed_list(line))
            elif cnt > MAX_HEIGHT + 1:
                instructions.append(process_instructions(line))
    list_of_stacks = create_stack(stack_lines)
    for instruction in instructions:
        list_of_stacks = apply_instruction_2(list_of_stacks, instruction)

    print("".join((top_of_each_stack(list_of_stacks))))


if __name__ == "__main__":
    main()
