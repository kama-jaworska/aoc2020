import numpy as np
import pandas as pd


def read_input(input_file):
    terrain = open(input_file, "r").read().splitlines()
    df = pd.DataFrame(np.array(np.array([[t for t in line] for line in terrain])))

    return df


def traverse_terrain(step, df):
    coords = [0, 0] # [row, column]
    tree_counter = 0

    while coords[0] < df.shape[0]: # until the loop reaches the vertical end of the terrain
        terrain_found = df.at[coords[0], coords[1]%df.shape[1]]

        if terrain_found == "#":
            tree_counter += 1

        # go to next step on the slope
        coords[0] += step[0]
        coords[1] += step[1]

    return tree_counter


def main(filename, slope_list):
    df = read_input(filename)
    results = []
    for step in slope_list:
        trees_found = traverse_terrain(step, df)
        print("Traversed slope", step, " and encountered ", trees_found, " trees.")
        results.append(trees_found)

    solution = np.product(results)
    print("Puzzle solution: ", solution)


if __name__ == "__main__":
    filename = "input.txt"
    slope_list = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    main(filename, slope_list)




