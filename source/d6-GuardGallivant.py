from utils import read_input_file

GUARD_CHAR = "^"
OBSTACLE_CHAR = "#"

DIRECTION_CHANGES = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def _get_guard_position(area: list[list[str]]) -> tuple[int, int]:
    location = (-1, -1)
    i = 0
    while i < len(area) and location == (-1, -1):
        if GUARD_CHAR in area[i]:
            location = (i, area[i].index(GUARD_CHAR))
        i += 1
    return location


def _take_step(start_position: tuple[int, int], step: tuple[int, int]) -> tuple[int, int]:
    return start_position[0] + step[0], start_position[1] + step[1]


def _is_within_bounds(area: list[list[str]], position: tuple[int, int]) -> bool:
    return (-1 < position[0] < len(area[0])) and (-1 < position[1] < len(area))


if __name__ == "__main__":
    print("Day 6:")
    map_area = read_input_file("d6-input.txt")

    # 1. find the guard's starting position - maintain to be used on 2nd part
    initial_guard_position = _get_guard_position(map_area)

    guard_position = initial_guard_position
    visited_positions: set[tuple[int, int]] = {guard_position}
    # 2. step until an obstacle is encountered
    direction_step = (-1, 0)  # going "upwards" first
    next_position = _take_step(guard_position, direction_step)

    while _is_within_bounds(map_area, next_position):
        next_position_char = map_area[guard_position[0] + direction_step[0]][guard_position[1] + direction_step[1]]
        if next_position_char == OBSTACLE_CHAR:
            # only switch directions
            direction_step = DIRECTION_CHANGES[direction_step]
            next_position = _take_step(guard_position, direction_step)
        else:
            # a. update guard position
            guard_position = next_position
            # b. add new guard position to visited positions
            visited_positions.add(guard_position)
        next_position = _take_step(guard_position, direction_step)

    print(f"{len(visited_positions)=}")

    # 3. Only all visited positions have to potential to create a loop by placing an obstacle
    potential_obstacle_positions = {vp for vp in visited_positions if vp != initial_guard_position}
    looping_positions = 0
    for potential_obstacle_position in potential_obstacle_positions:  # TODO: exclude starting position
        # initialize simulation
        simulation_area = [[char for char in line] for line in map_area]
        guard_position = initial_guard_position
        # 3a. place obstacle
        simulation_area[potential_obstacle_position[0]][potential_obstacle_position[1]] = "#"
        # 3b. get starting step
        direction_step = (-1, 0)  # going "upwards" first
        next_position = _take_step(guard_position, direction_step)
        route: set[tuple[tuple[int, int], tuple[int, int]]] = {(guard_position, direction_step)}

        # 3b. run route simulation
        while _is_within_bounds(simulation_area, next_position):
            next_position_char = simulation_area[guard_position[0] + direction_step[0]][guard_position[1] + direction_step[1]]
            if next_position_char == OBSTACLE_CHAR:
                # only switch directions
                direction_step = DIRECTION_CHANGES[direction_step]
                next_position = _take_step(guard_position, direction_step)
            else:
                # a. update guard position
                guard_position = next_position
                # b. if it's a new move add it to route and get next position to investigate, otherwise stop simulation
                if not (guard_position, direction_step) in route:
                    route.add((guard_position, direction_step))
                    next_position = _take_step(guard_position, direction_step)
                else:
                    looping_positions += 1
                    break
    print(f"{looping_positions=}")
