from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        output = [1] * (rowIndex + 1)

        for first_index in range(2, rowIndex + 1):
            for second_index in range(1, first_index):
                output[first_index - second_index] += output[first_index - second_index - 1]

        return output


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        0,  # [1]
        1,  # [1,1]
        2,  # [1,2,1]
        3,  # [1,3,3,1]
        4,  # [1,4,6,4,1]
        5,  # [1,5,10,10,5,1]
        6,  # [1,6,15,20,15,6,1]
    ]

    for input_array in inputs:
        output = solution.getRow(input_array)
        print(output)
