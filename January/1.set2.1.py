def reverse_and_check_palindrome(s):
    
    reversed_string = s[::-1]
   
    if s == reversed_string:
        return True, reversed_string
    else:
        return False, reversed_string


string = input("enter the string: ")
is_palindrome, reversed_string = reverse_and_check_palindrome(string)
print("Reversed string:", reversed_string)
print("Is palindrome:", is_palindrome)
