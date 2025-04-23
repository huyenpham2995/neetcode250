def isPalindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1

    while start <= end:
        if s[start].isalnum() and s[end].isalnum():
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        else:
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1
    return True