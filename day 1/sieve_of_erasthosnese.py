import math

def sieve(n):
    # Create a list where index represents the number
    # True = assume prime initially
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Main sieve logic:
    # Traverse only through numbers that are still marked as prime.
    # For each prime i, mark all multiples of i starting from i*i as non-prime.
    #
    # Why start from i*i?
    # Because all smaller multiples (2*i, 3*i, ..., (i-1)*i) 
    # were already marked by smaller primes.
    #
    # Time Complexity:
    # O(n log log n) — very efficient for large n.

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:  # Only proceed if i is prime
            # Mark all multiples of i as not prime
            # starting from i*i to n, stepping by i.
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Print all primes up to n
    for i in range(2, n + 1):
        if is_prime[i]:
            print(i)


if __name__ == "__main__":
    sieve(39)
