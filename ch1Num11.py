import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return  n * factorial(n - 1)
def approx(n):
    k = 0 
    #k is from given formula
    result = 0
    #doing the summation
    while k >= 0:
        result += ((factorial(4 * k) * (1103 + 26390 * k)) / ((factorial(k) ** 4) * (396 ** (4 * k))))
        
        #making sure this shit works 
        if k == 0:
            break
    answer = (1 / ((2 * math.sqrt(2) / 9801) * result))
    return answer
print(approx(0))
print(approx(1))
print(math.pi)
     
     
     