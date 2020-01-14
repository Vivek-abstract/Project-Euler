# Returns True if number is pallindrome
def is_pallindrome(s):
    length = len(s)
    for i in range(length//2):
        if s[i] != s[length-i-1]:
            return False
    return True

max_pallindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if is_pallindrome(str(product)):
            if product > max_pallindrome:
                max_pallindrome = i * j

print(max_pallindrome)