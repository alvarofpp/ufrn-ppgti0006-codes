from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(lambda: [])

        for string in strs:
            letters_set = str(sorted(string))
            hash_key = hash(letters_set)
            output[hash_key].append(string)

        return list(output.values())


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
        ['ddddddddddg', 'dgggggggggg'],
    ]

    for input_array in inputs:
        output = solution.groupAnagrams(input_array)
        print(output)
