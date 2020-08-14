""" created by Sarvesh kumar sharma """

'''implementation of the Radix sort algorithm in Python'''

from typing import List


def radix_sort(list_of_ints: List[int]) -> List[int]:
    RADIX = 10
    placement = 1
    max_digit = max(list_of_ints)
    while placement < max_digit:
        # declare and initialize empty buckets
        buckets = [list() for _ in range(RADIX)]
        # split list_of_ints between the buckets
        for i in list_of_ints:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # put each buckets' contents into list_of_ints
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                list_of_ints[a] = i
                a += 1
        # move to next
        placement *= RADIX
    return list_of_ints


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(radix_sort(unsorted))
