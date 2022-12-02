
# Read in the file
file_path = "../data.txt"
elves = []
current_elf = 0
# Read file line by line
with open(file_path) as fp:
    for cnt, line in enumerate(fp):
        line.strip()
        if line != "\n":
            current_elf += int(line)
        else:
            elves.append(current_elf)
            current_elf = 0

sorted_elves = sorted(elves, reverse=True)
print(sum(sorted_elves[0:3]))