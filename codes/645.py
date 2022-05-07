from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Duplicate
        counter = Counter(nums)
        duplicate = counter.most_common(1)[0][0]
        nums_set = set(sorted(nums))

        # Missing
        missing = None
        for index, number in enumerate(nums_set):
            expected_number = index + 1
            if expected_number != number:
                missing = expected_number
                break

        if missing is None:
            missing = len(nums)

        return [duplicate, missing]


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [1, 2, 2, 4],  # [2,3]
        [1, 1],  # [1,2]
        [2, 2],  # [2,1]
        [3, 2, 2],  # [2,1]
        [3, 2, 3, 4, 6, 5],  # [3, 1]
        [1, 5, 3, 2, 2, 7, 6, 4, 8, 9],  # [2, 10]
    ]

    for input_array in inputs:
        output = solution.findErrorNums(input_array)
        print(f'{output}')
