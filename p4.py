def p4():
    return max(a*b
               for a in range(100 ,1000)
               for b in range(100, 1000)
               if palindrome(str(a*b)))

def palindrome(string):
    return string == string[::-1]
