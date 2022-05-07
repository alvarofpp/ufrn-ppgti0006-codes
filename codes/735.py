from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []

        for asteroid in asteroids:
            while output and asteroid < 0 < output[-1]:
                if output[-1] < -asteroid:
                    output.pop()
                    continue
                elif output[-1] == -asteroid:
                    output.pop()
                break
            else:
                output.append(asteroid)

        return output


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [5, 10, -5],  # [5,10]
        [8, -8],  # []
        [10, 2, -5],  # [10]
        [-2, -1, 1, 2],  # [-2,-1,1,2]
    ]

    for input_array in inputs:
        output = solution.asteroidCollision(input_array)
        print(f'{output}')
