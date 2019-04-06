def create_test_paths():
    import random

    with open("q_2_large.txt", "w") as out_file:
        out_file.write("100\n")
        for _ in range(0, 100):
            grid_size = random.randint(2, 10)
            out_file.write(str(grid_size) + "\n")
            path = list("S" * ((grid_size * 2 - 2) // 2) + "E" * ((grid_size * 2 - 2) // 2))
            random.shuffle(path)
            out_file.write("".join(path) + "\n")


def print_grid(grid):
    for grid_row in grid:
        print(grid_row)
    print()


def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        size_of_grid = int(input())
        path = list(input())
        new_path = []

        grid = [["0"] * size_of_grid for _ in range(size_of_grid)]

        grid_x = 0
        grid_y = 0
        for path_direction in path:
            if path_direction == "E":
                grid[grid_y][grid_x] = "E"
                grid_x += 1
                new_path.append("S")
            elif path_direction == "S":
                grid[grid_y][grid_x] = "S"
                grid_y += 1
                new_path.append("E")

        print("Case #{}: {}".format(case_id, "".join(new_path)))


def main_simple():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        path = list(input())

        new_path = ["E" if x == "S" else "S" for x in path]

        print("Case #{}: {}".format(case_id, "".join(new_path)))


if __name__ == '__main__':
    main()
    # main_simple()
    # create_test_paths()
