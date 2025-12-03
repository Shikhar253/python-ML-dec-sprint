
# def reverse_string(s):
#     if not isinstance(s,str):
#         raise TypeError("Input must be a string")
#     if len(s)<=1:
#         return s
#     rev=[] #empty list cuz list mutable
#     for i in range(len(s)-1,-1,-1):
#         rev.append(s[i]) #makes it O(n) instead of squared                 #normalfor loop to reverse string
#     return "".join(rev)
# if __name__=="__main__":
#     print(reverse_string("hello"))



# def reverse_string(s):
#     if not isinstance(s,str):
#         raise TypeError("Input must be a string")
#     if len(s)<=1:
#         return s
#     rev=[s[i] for i in range(len(s)-1,-1,-1)]                        # list comprehension to reverse string
#     return "".join(rev)
# if __name__=="__main__":
#     print(reverse_string("hello"))



# def reverse_string(s):
#     if not isinstance(s,str):
#         raise TypeError("Input must be a string")
#     return s[::-1]                                              # Slicing creates a reversed copy
# if __name__=="__main__":
#     print(reverse_string("hello"))                            # It's implemented in optimized C loops under the hood, making it very efficient.

                                                                        

                                                                   

        
            


        
            

        
            