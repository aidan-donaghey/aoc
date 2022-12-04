choices_to_score = { "A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}

file_path = "data.txt"
total_score_1 = 0
total_score_2 = 0

def get_score_for_round_1(our_choice, their_choice):
    score  =  choices_to_score[our_choice]
    # Draw Condition
    if choices_to_score[our_choice] == choices_to_score[their_choice]:
        score += 3
        return score
    # LOSS CONDITION
    # R , P                  P, S               S, R
    elif  (their_choice == "A" and our_choice == "Y") or (their_choice == "B" and our_choice == "Z") or (their_choice == "C" and our_choice == "X"):

        score += 6
        return score
    # WIN CONDITION
    # R, S                   S, P               P, R
    elif (their_choice == "A" and our_choice == "Z") or (their_choice == "B" and our_choice == "X") or (their_choice == "C" and our_choice == "Y"):
        score += 0
        return score


def get_score_for_round_2(our_choice, their_choice):
    # LOSS
    if our_choice == "X":
        if their_choice == "A":
            print("Loss and we expect a score of 3")
            return  3
        elif their_choice == "B":
            print("Loss and we expect a score of 1")
            return  1
        elif their_choice == "C":
            print("Loss and we expect a score of 2")
            return  2

    # DRAW
    if our_choice == "Y":
        score = 3
        score += choices_to_score[their_choice]
        print(f"Draw and we expect a score of {score}")
        return score
    #WIN
    if our_choice == "Z":
        score = 6
        if their_choice == "A":
            print(f"Win and we expect a score of {score + 2}")
            return score + 2
        elif their_choice == "B":
            print(f"Win and we expect a score of {score + 3}")
            return score + 3
        elif their_choice == "C":
            print(f"Win and we expect a score of {score + 1}")
            return score + 1





with open(file_path) as fp:
    for cnt, line in enumerate(fp):
        line = line.strip()
        print(line)
        total_score_1 += get_score_for_round_1(line[2], line[0])
        total_score_2 += get_score_for_round_2(line[2], line[0])


print(total_score_1)
print(total_score_2)

