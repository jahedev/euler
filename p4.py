"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome(n):
    half = int(len(str(n))/2)
    number = list(str(n))

    is_palindrome = True

    for i in range(1,half+1):
        #print(number[i-1], number[(-1)*i])
        if number[i-1] != number[(-1)*i]:
            is_palindrome = False
    
    return is_palindrome

def find_3digit_palindromes():
    pals = []
    print("Searching for palindromes . . .")
    for i in range(999, 99, -1):
        for j in range(100, 999+1):
            test_num = i * j
            if palindrome(test_num):
                #print('%d * %d = %d' % (i, j, test_num))
                pals.append(test_num)
    print("Done.")
    return pals

print(max(find_3digit_palindromes()))