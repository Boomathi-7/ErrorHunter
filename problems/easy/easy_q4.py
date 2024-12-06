# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative" 
    else:
        return "Number is Zero" 
        
if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    res = check_number(num)
    print(res)
    
    
    