from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        output = []
        nums.sort()

        for first_index in range(len(nums)):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue

            second_index = first_index + 1
            third_index = len(nums) - 1
            required_sum = 0 - nums[first_index]

            while second_index < third_index:
                current_sum = nums[second_index] + nums[third_index]

                if current_sum < required_sum:
                    second_index += 1
                elif current_sum > required_sum:
                    third_index -= 1
                else:
                    output.append([nums[first_index], nums[second_index], nums[third_index]])
                    second_index += 1
                    while second_index < third_index \
                            and nums[second_index] == nums[second_index - 1]:
                        second_index += 1

        return output


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [-1, 0, 1, 2, -1, -4],  # [[-1,-1,2],[-1,0,1]]
        [],  # []
        [0],  # []
        [0, 0, 0],  # [[0,0,0]]
        [1, -1, -1, 0],  # [[-1,0,1]]
    ]

    for input_array in inputs:
        output = solution.threeSum(input_array)
        print(output)
