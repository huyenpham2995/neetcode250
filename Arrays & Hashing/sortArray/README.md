# Question
https://leetcode.com/problems/sort-an-array/

# Thoughts:
Time for me to review all the sort algorithm I know.

## Bubble Sort
The slowest of them all. The smallest element slowly "bubble" up to the first position and so on.
- Start from the first element, compare it to the adjacent element and see which one is smaller. swap the smaller one before the bigger one.
- Keep doing it like that until reaching the end of the array.
- Keep doing step 1 and 2 for n times (n being the number of elements in the array). To improve this algorithm, we can also stop looping if there's no swap happened.

## Selection Sort
- Start with the first number. Check other numbers to see if anything is smaller than that number. If they are, swap.
- Continue to the next number and repeat the same thing from i+1 position.
- Do it until reaching the end of the array

## Merge Sort

## Heap Sort

## Quick Sort
- The idea is to oick a pivot, then partition the array to 2 separate parts: one array contains all elements that are less than or equal the pivot, the other contains elements that are larger than the pivot
- Sort the left array with the same algorithm
- Sort the right array with the same algorithm
- Merge left + pviot + right and return as the result.

# BigO
## Bubble Sort
- Time: worst time O(N^2), best time when the array is already sorted N.
- Space: in place swapping, O(1)

## Selection Sort
- Time: O(N^2)
- Space: in place, O(1)

## Merge Sort

## Heap Sort

## Quick Sort
- BigO: worst case O(N^2) (depends on how we choose the pivot), best case O(N)
- Space: O(N)
