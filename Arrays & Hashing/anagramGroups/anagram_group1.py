from collections import defaultdict
from typing import List

def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    res_dict = defaultdict(list)

    for s in strs:
        processed = False
        for k in res_dict:
            if isAnagram(s,k):
                res_dict[k].append(s)
                processed = True
                break
        if not processed:
            res_dict[s].append(s)

    return [v for _,v in res_dict.items()]

def isAnagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
            return False
    c_count = {}
    for c in s1:
        if c not in c_count:
            c_count[c] = 0
        c_count[c] += 1
    for c in s2:
        if c not in c_count:
            return False
        c_count[c] -= 1
        if c_count[c] == 0:
            c_count.pop(c,None)
    return True
            