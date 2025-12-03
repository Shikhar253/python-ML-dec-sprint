# def factorial(n):
#     #negative nos.
#     if n < 0:
#         raise ValueError("Factorial not defined for negative integers")
#     ans = 1
#     # while loop
#     # i = n
#     # while i > 1:
#     #     ans  *= i 
#     #     i -= 1
#     # return ans
    
#     #for loop
#     # for i in range (n,1,-1):
#     #     ans*=i
#     # return ans
    
    
    
    
    
    
    
# if __name__=="__main__":  
#     print(factorial(9))


#recursive
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative integers")
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
   
    

    
if __name__=="__main__":  
    print(factorial(6))