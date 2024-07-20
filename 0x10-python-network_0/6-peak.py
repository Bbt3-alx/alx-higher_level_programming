#!/usr/bin/python3
"""A module with 2 function to finds a peak number"""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers."""
    def binary_search(nums, left, right):
        """Binary search function"""
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            return binary_search(nums, mid + 1, right)
        else:
            return binary_search(nums, left, mid)

    if not list_of_integers:
        return None

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
