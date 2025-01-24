from utils import read_input_file
from itertools import combinations

if __name__ == "__main__":
    print("Day 5:")
    input_rules = read_input_file("d5-input-rules.txt")
    input_sequences = read_input_file("d5-input-sequences.txt")

    rules_by_pages = [[int(page) for page in rule.split("|")] for rule in input_rules]
    sequences_by_pages = [[int(page) for page in print_sequence.split(",")] for print_sequence in input_sequences]

    correct_middle_number_sum = 0
    incorrect_middle_number_sum = 0

    for sequence in sequences_by_pages:
        # 1. make permutations
        page_combinations = [c for c in combinations(sequence, 2)]
        # 2. get rules applying to current sequence
        sequence_rules = []
        for rule in rules_by_pages:
            # if any of the combinations have both pages in a rule, add that rule to the sequence rules
            if any(all((c in rule) for c in combination) for combination in page_combinations):
                sequence_rules.append(rule)
        # 3. check if sequence is properly ordered
        # checks if all pages are in the correct order by comparing the indexes of the supposed first to the supposed second
        is_correctly_ordered = all((sequence.index(rule[0]) < sequence.index(rule[1])) for rule in sequence_rules)

        # 4. add middle number of correctly ordered sequences to the respective sum
        if is_correctly_ordered:
            correct_middle_number_sum += sequence[(len(sequence) // 2)]
        # 5. fix order of incorrectly ordered sequences and add middle number of corrected sequence to the respective sum
        else:
            # get and apply not satisfied rules repeatedly until all are satisfied
            not_satisfied_rules = [rule for rule in sequence_rules if not (sequence.index(rule[0]) < sequence.index(rule[1]))]

            while len(not_satisfied_rules) > 0:
                for rule in not_satisfied_rules:
                    # remove the page that should follow and add it after the leading page (by slicing)
                    sequence.remove(rule[1])
                    sequence = sequence[: sequence.index(rule[0]) + 1] + [rule[1]] + sequence[sequence.index(rule[0]) + 1 :]
                not_satisfied_rules = [rule for rule in sequence_rules if not (sequence.index(rule[0]) < sequence.index(rule[1]))]
            incorrect_middle_number_sum += sequence[(len(sequence) // 2)]

    print(f"[>] Sum of correctly ordered sequences' middle numbers: {correct_middle_number_sum}")
    print(f"[>] Sum of corrected sequences' middle numbers: {incorrect_middle_number_sum}")
