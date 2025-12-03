def even_odd_printer():
    for i in range (1,11):
        status = "Even" if i%2==0 else "Odd"
        print(f"{i} {status}")
        
if __name__=="__main__":
    even_odd_printer()