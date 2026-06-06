import collections
def isAnagram(s: str, t: str) ->bool:
    if len(s) != len(t):
        return False
    
    count = collections.Counter(s)
    for ch in t:
        count[ch]-=1
        if count[ch]<0:
            return False
    
    return True

s = "anagram"
t = "nagaram"   
print(isAnagram(s, t))