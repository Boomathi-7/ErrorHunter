# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    result = 1
    while n > 0:
        result *= n
        n -= 1   
    return result

if __name__ == "__main__":
    num = int(input("Enter the Number :"))
    res = factorial(num)
    print(res)
