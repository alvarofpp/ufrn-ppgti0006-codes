from itertools import chain, combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(chain.from_iterable(combinations(nums, index) for index in range(len(nums) + 1)))


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [1, 2, 3],  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        [0],  # [[],[0]]
    ]

    for input_array in inputs:
        output = solution.subsets(input_array)
        print(output)
