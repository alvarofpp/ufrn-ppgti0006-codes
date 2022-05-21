# NOT WORKING
from typing import List


class Solution:
    def find_and_join(self, families_set: List, relative_tuple, new_tuple) -> None:
        relative_tuple = hash(relative_tuple)
        new_tuple = hash(new_tuple)

        for family_set in families_set:
            if relative_tuple in family_set:
                family_set.add(new_tuple)
                return
            if new_tuple in family_set:
                family_set.add(relative_tuple)
                return
        families_set.append({relative_tuple, new_tuple})

    def check_intersections(self, families_set) -> List:
        output = []

        for family_set in families_set:
            if len(output) == 0:
                output = [family_set]
                continue

            other_family = True
            for index, family in enumerate(output):
                if family_set.intersection(family):
                    output[index] = set.union(family, family_set)
                    other_family = False
                    break

            if other_family:
                output.append(family_set)

        return output

    def numIslands(self, grid: List[List[str]]) -> int:
        families_set = []
        max_rows = len(grid)
        max_columns = len(grid[0])

        for row, row_values in enumerate(grid):
            for column, value in enumerate(row_values):
                if value == '0':
                    continue

                coordinate = (row, column)
                new_family = True

                # Left
                if column - 1 >= 0 and grid[row][column - 1] == '1':
                    new_family = False
                    self.find_and_join(families_set, (row, column - 1), coordinate)
                # Top
                if row - 1 >= 0 and grid[row - 1][column] == '1':
                    new_family = False
                    self.find_and_join(families_set, (row - 1, column), coordinate)
                # Bottom
                if row + 1 < max_rows and grid[row + 1][column] == '1':
                    new_family = False
                    self.find_and_join(families_set, (row + 1, column), coordinate)
                # Right
                if column + 1 < max_columns and grid[row][column + 1] == '1':
                    new_family = False
                    self.find_and_join(families_set, (row, column + 1), coordinate)
                # New family
                if new_family:
                    families_set.append({hash(coordinate)})

        output = self.check_intersections(families_set)
        output = self.check_intersections(output)

        return len(output)


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ],  # 1
        [
            ['1', '0', '1', '1', '1'],
            ['1', '0', '1', '0', '1'],
            ['1', '1', '1', '0', '1'],
        ],  # 1
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ],  # 3
        [
            ['1', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0'],
            ['0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1'],
            ['1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '1', '1', '0'],
            ['0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '1', '1'],
            ['1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1'],
            ['0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0'],
            ['1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '1', '0'],
            ['0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1'],
            ['0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0'],
            ['0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0'],
            ['1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
            ['0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1'],
            ['1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0'],
            ['0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0'],
            ['0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1'],
            ['0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '0', '1'],
            ['0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
            ['0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1'],
            ['0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0'],
        ],  # 23
    ]

    for input_array in inputs:
        output = solution.numIslands(input_array)
        print(output)
