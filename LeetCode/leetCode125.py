# import string

# s = "A man, a plan, a canal: Panama"

# m = str.maketrans('', '', string.punctuation)
# S = s.translate(m)

# S = S.lower()
# S = S.replace(" ", "")

# t = S[::-1]

# if S == t:
#     print(True)
# else:
#     print(False)


# import re
# s = "A man, a plan, a canal: Panama"
# cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
# print(cleaned == cleaned[::-1])

import string

s = "A man, a plan, a canal: Panama"

# Clean the string
S = s.translate(str.maketrans('', '', string.punctuation))
S = S.lower().replace(" ", "")

# Check palindrome
print(S == S[::-1])  # Direct comparison