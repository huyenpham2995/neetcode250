# Question
https://leetcode.com/problems/top-k-frequent-elements/

# Thoughts
## Approach 1: dictionary and sort
- The easiest way is to go through the array, count the appearance of each number, record them in a dictionary. Then sort the dictionary by value and choose the top k appearances

## Approach 2: bucket sort
- This approach still requires counting the number of occurences of each number and store them in a dictionary.
- If the amount of **unique** numbers is <= k, then we can just return the list of set of the array. Eg: [1,1,1,2,3] and k=3, we can just return [1,2,3] since there are on;y 3 unique numbers, the top 3 is obviously them.
- The top frequent number has the maximum appearance of N times. So if we have an array where each slot represent the number of times then num in the array appears (slot 1 for num with 1 time appearance, slot N for num with N time appearance), we can access that slot in constant time. Let's call this array `bucket`.
    - Let's say each slot of the bucket is a list, because there might be more than 1 numbers with the same number of appearances.
- Go through the dictionary. Each entry has a `(k,v)` pair. Then we append `k` at position `v` (actually v-1 because of 0-index).

NOTE: a big thing that I learned from solving this question. When I initialize an array of empty arrays, I did `arr = [[]] * N`. This line of code creates an array of **the same empty array**, i.e, these empty arrays are pointing to the same location in the memory. So later when I said arr[i].append(num), ALL empty arrays inside have 1 appended to it. The correct way to **create N separate arrays** is `arr = [[] for i in range(N)]`.
- Go through the bucket array again from the back (the back represent the most number of appearances) and pick out k numbers from it, then return the list of k numbers.

# BigO
- Time: O(3N) -> O(N)
- Space: O(2N) (dictionary + bucket array) -> O(N)