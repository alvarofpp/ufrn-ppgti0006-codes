from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        len_string = len(s)
        dna_sequence_num = 10

        if len_string <= dna_sequence_num:
            return []

        output = []
        dna_set = set()

        for i in range(len_string - dna_sequence_num + 1):
            dna_string = s[i:i + 10]
            dna_hash = hash(dna_string)

            if dna_hash not in dna_set:
                dna_set.add(dna_hash)
                continue

            output.append(dna_string)

        return list(set(output))


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',  # ["AAAAACCCCC","CCCCCAAAAA"]
        'AAAAAAAAAAAAA',  # ["AAAAAAAAAA"]
        'AAAAAAAAAAA',  # ["AAAAAAAAAA"]
    ]

    for input_array in inputs:
        output = solution.findRepeatedDnaSequences(input_array)
        print(output)
