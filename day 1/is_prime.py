import math

def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    number = 66

    if is_prime(number):
        print(f"{number} is Prime")
    else:
        print(f"{number} is Not Prime")
