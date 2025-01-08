def get_number():
    
    num = int(input("Enter a number: "))
    return num

def is_armstrong(num):
    
    num_str = str(num)
    num_digits = len(num_str)
    
   
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
   
    if sum_of_powers == num:
        return True
    else:
        return False


number = get_number() 
if is_armstrong(number): 
    print(f"{number} is an Armstrong number.")
else:
     print(f"{number} is not an Armstrong number.")
