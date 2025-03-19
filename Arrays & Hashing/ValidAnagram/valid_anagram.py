from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dict_t = defaultdict(int)
    for char_t in t:
        dict_t[char_t] += 1
    
    for char_s in s:
        if dict_t[char_s] < 1:
            return False
        dict_t[char_s] -= 1
        if dict_t[char_s] == 0:
            dict_t.pop(char_s, None)
            
    return True