
def palindrome(word):
    edited = ''.join(ch for ch in word if ch.isalpha()).lower()
    for i in range(len(edited)):
        if edited[i] != edited[-i-1]:
            return False
    return True
    

print(palindrome("eye"))