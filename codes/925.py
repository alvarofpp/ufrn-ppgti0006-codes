from typing import List


class Solution:
    def count_letters_in_order(self, string: str) -> List:
        last_letter = None
        index = 0
        typed_values = []

        for letter in string:
            if last_letter is None:
                typed_values.append([letter, 1])
                last_letter = letter
                continue

            if letter == last_letter:
                index_value = typed_values[index]
                typed_values[index] = [index_value[0], index_value[1] + 1]
                continue

            index += 1
            typed_values.append([letter, 1])
            last_letter = letter

        return typed_values

    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_count = self.count_letters_in_order(name)
        typed_count = self.count_letters_in_order(typed)

        if len(name_count) != len(typed_count):
            return False

        output = True

        for index, values in enumerate(name_count):
            typed_values = typed_count[index]
            if values[0] != typed_values[0] or values[1] > typed_values[1]:
                output = False
                break

        return output


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        ['alex', 'aaleex'],  # true
        ['saeed', 'ssaaedd'],  # false
        ['rick', 'kric'],  # false
        ['alex', 'aaleexa'],  # false
    ]

    for input_array in inputs:
        output = solution.isLongPressedName(input_array[0], input_array[1])
        print(output)
