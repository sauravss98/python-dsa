"""
Module for finding indices of two numbers that add up to a target.
"""

class Solution:
    """
    Solution class for solving the Two Sum problem.
    """
    @staticmethod
    def two_sum(nums, target):
        """
        Find two numbers in the list `nums` that add up to the `target`.

        Args:
            nums (list): A list of integers.
            target (int): The target sum.

        Returns:
            list: Indices of the two numbers that add up to the target.
        """
        seen = {}
        for i, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [seen[complement], i]
            
            seen[value] = i
        
        return []  # Return an empty list if no solution is found.

# Example usage of the two_sum function.
if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = 9
    indices = Solution.two_sum(nums, target)
    print(f"The indices of the two numbers that add up to {target} are: {indices}")
