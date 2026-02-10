def addBinary(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    
    # Process both numbers from right to left
    while i >= 0 or j >= 0 or carry:
        # Get digits (0 if beyond length)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # Sum with carry
        total = digit_a + digit_b + carry
        
        # Current digit and new carry
        current_digit = total % 2
        carry = total // 2
        
        # Add to result (at beginning since we're processing backwards)
        result.append(str(current_digit))
        
        # Move to next digits
        i -= 1
        j -= 1
    
    # Reverse and join (since we processed from right to left)
    return ''.join(reversed(result))

a = '101111001'
b = '111111111'

x = addBinary(a,b)
print(x)