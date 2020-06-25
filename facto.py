# num = 10
# factorial = 1
# summ = 0
# for i in range(1, num+1):
#     factorial = factorial *i 
    
    
#     summ += int(factorial%10) 
#     n = int(factorial/10) 
#     print(summ)
  
def getSum(num): 
    
    factorial = 1
    summ = 0
    for i in range(1, num+1):
        factorial = factorial *i 
   
  
    # Single line that calculates sum  
    while(factorial > 0): 
        summ += int(factorial%10) 
        factorial = int(factorial/10) 
  
    return summ
 
# Driver code 
num = 100
# n = 687
print(getSum(num))
   
