def strStr(haystack, needle):
    x = len(needle)
    for i in range(len(haystack)):
        if haystack[i:x+i] == needle:
            return i
    return -1

haystack = "sadbutsab"
needle = "mad"

y = strStr(haystack, needle)
print(y)