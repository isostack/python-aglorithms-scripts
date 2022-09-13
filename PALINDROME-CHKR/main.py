def palindrome(str):
    return str == ''.join([str[num * -1] for num in range(1 , len(str) + 1 )])

print(palindrome("eye")) 
print(palindrome("racecar")) 
print(palindrome("madam")) 
print(palindrome("anna")) 
print(palindrome("neveroddoreven")) 
