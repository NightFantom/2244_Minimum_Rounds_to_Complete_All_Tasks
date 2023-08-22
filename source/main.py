from collections import defaultdict


class Solution:

    def minimumRounds(self, array):
        storage = defaultdict(lambda: 0)
        for el in array:
            storage[el] = storage[el] + 1

        not_divided = False
        turns = 0
        for task_cost, amount in storage.items():
            remain_3 = amount % 3
            if remain_3 == 0:
                turns += amount // 3
            elif remain_3 == 1:
                if amount == 1:
                    not_divided = True
                    break
                else:
                    turns += amount // 3 - 1 + 2
            else:
                turns += amount // 3 + 1

        return -1 if not_divided else turns


if __name__ == "__main__":
    array = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    result = Solution().minimumRounds(array)
    print(result)
