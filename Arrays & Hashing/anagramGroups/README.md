# Question
https://neetcode.io/problems/anagram-groups

# Thoughts
- My approach:
    - Create a function to see if 2 words are anagram of each other (O(m), with m being the number characters of the longest word)
    - Create a dictionary with the key as the first (the "representative") of the anagram group. Eg: "eat" is the representative of "ate" or "tea".
    - Go through the list of string, see if it is the anagram with any of the representative words. If it is, add it to the list. If not, make it a key, also add itself to the list (O(n^2), with n being the # of words in strs list).
    - Return the array of values of the dictionary
- Better approach:
    - The better way to also to ultilize dictionary but in a different way. Create an array of 26 slots, equivalent to 26 characters (can increase this if there's special characters), set all of them to 0 by default (their count).
    - For each word in the strs array, count the number of each characters and set the count in the array above.
    - Change the array into a set (eg: [0,0,1,...,2,1,0] -> (0,1,2,1)) and use that set to be the key of the dictionary. The value will be the list of words that have that same key.
    - Return the result

# BigO
- My approach: 
    - Time: O(n^2 * m)
    - Space: O(n)