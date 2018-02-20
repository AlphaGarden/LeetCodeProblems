# Brute Fore version
class Solution:
    def __init__(self):
        self.memo = {}

    # Time complexity  will 2^n base on the recursive tree
    def knapsack_brute(self, values, weights, W, pos):
        # Base case if W is 0 , then return 0
        if W == 0 or pos == -1:
            return 0
        else:
            """
            Case 1: Include the current item and then subtract the weight in addiction update the pos to the previous one
            Case 2: Exclude the current item and then update the pos to the previous item
            """
            include = values[pos] + self.knapsack_brute(values, weights, W - weights[pos], pos - 1)
            exclude = self.knapsack_brute(values, weights, W, pos - 1)
            return max(include, exclude)

    def knapsack_dp(self, values, weights, W, pos):
        if W == 0 or pos == -1:
            return 0
        else:
            if self.memo.has_key((pos, W)):
                return self.memo[(pos, W)]
            else:
                include = values[pos] + self.knapsack_brute(values, weights, W - weights[pos], pos - 1)
                exclude = self.knapsack_brute(values, weights, W, pos - 1)
                self.memo[(pos, W)] = max(include, exclude)
                return self.memo[(pos, W)]


if __name__ == '__main__':
    solution = Solution()
    test_case_weights = [10, 20, 30]
    test_case_values = [60, 100, 120]
    capacity = 50
    print solution.knapsack_brute(test_case_values, test_case_weights, capacity, len(test_case_weights) - 1)
    print solution.knapsack_dp(test_case_values, test_case_weights, capacity, len(test_case_weights) - 1)