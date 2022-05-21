from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        jump = 0

        while index < len(nums) and index <= jump:
            jump = max(jump, index + nums[index])
            index += 1

        return index == len(nums)


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [2, 3, 1, 1, 4],  # true
        [3, 2, 1, 0, 4],  # false
    ]

    for input_array in inputs:
        output = solution.canJump(input_array)
        print(output)
