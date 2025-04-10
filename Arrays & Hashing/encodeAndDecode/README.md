# Question
https://neetcode.io/problems/string-encode-and-decode

# Thoughts
- Encode: when we want to encode something, there should be a separator between the words we want to encode so later on that separator can help with the decoding process.
    - Whatever separator we are choosing, there will be a chance that the separator will be included in one of the string in the array.
    - To fix this issue, we can add another separator, which is the length of the word. So for example, the word "need" will be "4#need" after encoding. Later on we know if we hits a "#" (the separator), the next 4 characters belong to the word after encoding.
- Decode:
    - Detect to see where is the digit, that will be the length of the word (call this M)
    - If a separator is detected, the next M characters belong to the word. Add that to the result.

# BigO
- Encode:
    - Time: O(N)
    - Space: O(N)
- Decode:
    - Time: O(N+M) (M is the amount of digits and separators used)
    - Space: O(N)