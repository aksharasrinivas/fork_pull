def find_factorial_loop(n):
    if n < 0:
        return "Not defined for negative numbers."
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        
    return factorial
if num<0:
 print("no negative numbers")
 exit()

print(find_factorial_loop(5))  
