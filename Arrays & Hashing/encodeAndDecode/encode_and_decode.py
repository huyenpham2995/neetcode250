from typing import List

def encode(strs: List[str]) -> str:
    encoded_str = ""
    separator = "#"

    for s in strs:
        encoded_str += str(len(s)) + separator + s
    return encoded_str

def decode(s: str) -> List[str]:
    i=0
    res = []

    while i < len(s):
        count = ""
        while s[i].isdigit():
            count += s[i]
            i += 1
        count = int(count)
        if s[i] == "#":
            i += 1
            res.append(s[i:i+count])
            i += count
    return res