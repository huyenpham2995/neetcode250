from collections import defaultdict
from typing import List

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    res_dict = defaultdict(list)

    for word in strs:
        c_count = [0]*26
        for c in word:
            c_count[ord(c) - ord('a')] += 1
        res_dict[tuple(c_count)].append(word)
    
    return [v for _,v in res_dict.items()]