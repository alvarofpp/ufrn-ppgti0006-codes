from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words.pop())
        for word in words:
            counter = counter & Counter(word)

        output = []
        for data in counter.items():
            output = [*output, *[data[0] for index in range(data[1])]]

        return output


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        ['bella', 'label', 'roller'],  # ['e','l','l']
        ['cool', 'lock', 'cook'],  # ['c','o']
    ]

    for input_array in inputs:
        output = solution.commonChars(input_array)
        print(f'{output}')
