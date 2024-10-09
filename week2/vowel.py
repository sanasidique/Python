string=input("Enter the string: ")
print("The vowels are:")
for letter in string:
    if letter in 'aeiou':
        print(letter,end=" ")
