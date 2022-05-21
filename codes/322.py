from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = [0] + [amount + 1] * amount
        amount_one = amount + 1

        for coin in coins:
            for i in range(coin, amount_one):
                memory[i] = min(memory[i], memory[i - coin] + 1)

        return -1 if memory[amount] == amount_one else memory[amount]


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [[1, 2, 5], 11],  # 3
        [[2], 3],  # -1
        [[1], 0],  # 0
        [[186, 419, 83, 408], 6249],  # 20
    ]

    for input_array in inputs:
        output = solution.coinChange(input_array[0], input_array[1])
        print(output)
