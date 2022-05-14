from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)
        return min(counter_nums, key=counter_nums.get)


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [2, 2, 3, 2],  # 3
        [0, 1, 0, 1, 0, 1, 99],  # 99
    ]

    for input_array in inputs:
        output = solution.singleNumber(input_array)
        print(output)
