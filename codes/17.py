import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        lists_letters = [letters[digit] for digit in digits]
        return [''.join(combination) for combination in itertools.product(*lists_letters)]


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        '23',  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        '',  # []
        '2',  # ["a","b","c"]
    ]

    for input_array in inputs:
        output = solution.letterCombinations(input_array)
        print(output)
