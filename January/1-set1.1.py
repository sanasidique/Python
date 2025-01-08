

def count_and_replace_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    modified_string = ""
    
    # Iterate through each character in the string
    for char in s:
        if char in vowels:
            count += 1
            modified_string += "#"
        else:
            modified_string += char
    
    return count, modified_string

# Example usage
string = input("enter the string:")
vowel_count, modified_string = count_and_replace_vowels(string)
print("Number of vowels:", vowel_count)
print("Modified string:", modified_string)
