from utils import read_input_file

XMAS_LENGTH = 4
XED_MAS_LENGTH = 3


def _get_direction_indexes_left_end(x: int, y: int, max_x: int, max_y: int, string_length: str) -> list[tuple[int, int]]:
    step_directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    all_direction_indexes = [[(x + x_dir * step, y + y_dir * step) for step in range(0, string_length)] for x_dir, y_dir in step_directions]
    valid_direction_indexes = [
        direction
        for direction in all_direction_indexes
        if all((step_x >= 0 and step_y >= 0) and (step_x < max_x and step_y < max_y) for step_x, step_y in direction)
    ]
    return valid_direction_indexes


def __get_direction_indexes_centered(x: int, y: int, max_x: int, max_y: int) -> list[tuple[int, int]]:
    step_directions = [[(1, -1), (0, 0), (-1, 1)], [(-1, -1), (0, 0), (1, 1)]]

    all_direction_indexes = [[(x + x_dir, y + y_dir) for x_dir, y_dir in direction] for direction in step_directions]
    valid_direction_indexes = [
        direction
        for direction in all_direction_indexes
        if all((step_x >= 0 and step_y >= 0) and (step_x < max_x and step_y < max_y) for step_x, step_y in direction)
    ]
    return valid_direction_indexes


if __name__ == "__main__":
    print("Day 4:")
    input = read_input_file("d4-input.txt")

    max_x = len(input)
    max_y = len(input[0])

    xmas_count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                direction_indexes = _get_direction_indexes_left_end(i, j, max_x, max_y, XMAS_LENGTH)
                candidate_xmas = ["".join([input[x][y] for x, y in candidate]) for candidate in direction_indexes]
                xmas_count += sum(1 for candidate in candidate_xmas if candidate == "XMAS")

    print(xmas_count)

    xed_mas_count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "A":
                direction_indexes = __get_direction_indexes_centered(i, j, max_x, max_y)
                candidate_xed_mas = ["".join([input[x][y] for x, y in candidate]) for candidate in direction_indexes]
                is_valid_xed_mas = len(candidate_xed_mas) == 2 and all((candidate == "MAS" or candidate == "SAM") for candidate in candidate_xed_mas)

                xed_mas_count += 1 if is_valid_xed_mas else 0

    # for i in range(136,140):
    #     print(input[i][110:130])
    # for li in input:
    #     print(li)
    print(xed_mas_count)
