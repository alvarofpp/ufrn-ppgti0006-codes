from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_length = len(citations)
        citations.sort()
        output = 0

        for index, citation_value in enumerate(citations):
            h_index = citations_length - index

            if citation_value >= h_index:
                output = h_index
                break

        return output


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [3, 0, 6, 1, 5],  # 3
        [1, 3, 1],  # 1
        [100],  # 1
        [0],  # 0
        [0, 1],  # 1
        [3, 0, 6, 1, 5, 5, 5, 5, 5],  # 5
        [11, 15],  # 2
    ]

    for input_array in inputs:
        output = solution.hIndex(input_array)
        print(output)
