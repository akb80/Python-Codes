def is_palindrome(num):
    return str(num) == str(num)[::-1]
print(is_palindrome(101))
print(is_palindrome(100))
