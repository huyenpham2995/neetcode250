# Question
https://leetcode.com/problems/valid-anagram/

# Thoughts
- For the 2 words to be anagram, they have to have the same number of characters, so if that fails, return False immediately.
- They will also have the same number of character. We don't care about the order of the characters, so just need to keep track of the number of characters.
- First going through word t and count the number of each characters. Store them in a dictionary (key: character, value: count)
- Then go through each character of s: 
    - If there's no character of s in the dictionary, return False immediately
    - If there is, deduct 1 from the count.
    - If the count goes back to 0, that character does not appear anymore in t, then it shouldn't in s, if they are anagram.
- At the end, if they have the same amount of characters and the count of each character, they are anagram

# BigO
- Space: store all characters in a dictionary. There are at most 26 characters (if we distinguish between upper and lowercase, then there will be 52). Even when we take into consideration special characters, the number is finite -> O(1)
- Time: go through each character of s once, each character of t once -> O(2N) -> O(N).