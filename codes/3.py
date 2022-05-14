class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_input = len(s)
        if len_input in [0, 1]:
            return len_input

        window = ''
        max_length = 0

        for char in s:
            if char in window:
                position = window.find(char) + 1
                window = window[position:]

            window += char
            max_length = max([len(window), max_length])

        return max_length


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        'abcabcbb',  # 3 abc
        'bbbbb',  # 1 b
        'pwwkew',  # 3 wke
    ]

    for input_array in inputs:
        output = solution.lengthOfLongestSubstring(input_array)
        print(output)
