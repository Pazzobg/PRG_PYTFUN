# Write a function which takes any number of parameters and returns their average.
def get_avg(*args):
    return (sum(args) * 1.0) / len(args)


result = get_avg(12, 5, 19, 2, 44)
# result = get_avg(7, 200, 3081, 43, 10, 65, 46, 4865, 35, -12, 5.6, -79.935, 60)
print(result)

# 1. Write a function to calculate Lucas numbers using the naïve recursion. Lucas numbers are very similar to Fibonacci
# numbers and are defined by L(0)=2, L(1)=1 and L(n)=L(n-1)+L(n-2)
# 2. Use a timing decorator to log how long each call. How long does it take to calculate L(35)? What about L(100)?
# 3. Now add a memoize decorator. Can you calculate L(100) now?
# 4. Write a function which does prime factorization of a number, e.g. 20633239 = 11*29*71*911. Calculate the prime
# factorization of L(60) and L(61).
import datetime as dt


def logger_decorator(orig_func):
    """Create a boolean var showing if function execution is being already timed. This way execution time is clocked
    only when the first and the last calls to the original function are executed, solving the problem with timing
    the execution of recursive function (when each of the recursive calls are being timed)."""
    is_timing = False

    def new_timed_func(*args):
        nonlocal is_timing
        if is_timing:
            return orig_func(*args)
        else:
            start = dt.datetime.now()
            is_timing = True
            value = orig_func(*args)
            is_timing = False
            end = dt.datetime.now()
            print(f"Start: {start}. End: {end}. Elapsed: {end - start}")
            return value

    return new_timed_func


def memoize_decorator(orig_func):
    """Create a dictionary for holding already calculated values. Function first checks if the current value was already
    calculated. Only if it wasn't, it is calculated and value is added to dictionary. Then it is returned."""
    stored_values = {}

    def new_memoized_func(*args):
        if args not in stored_values:
            value = orig_func(*args)
            stored_values[args] = value
        return stored_values[args]

    return new_memoized_func


# Comment out/in decorators as needed
@logger_decorator
@memoize_decorator
def get_nth_lucas_number(n: int) -> int:
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        a = get_nth_lucas_number(n - 1)
        b = get_nth_lucas_number(n - 2)
    return a + b


def get_prime_factors(n):
    """Function returns the prime factors of the number provided as an argument. E.g. 12 = 2*2*3"""
    factors = []
    i = 2
    while (i * i <= n):
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(get_nth_lucas_number(61))
print(get_prime_factors(get_nth_lucas_number(61)))


'''
Actual outputs from running the code: 
 
Without @memoize:
get_nth_lucas_number(35)
0:00:06.139359
20633239

get_nth_lucas_number(40)
0:01:08.291960
228826127

get_nth_lucas_number(45)
0:12:38.196051
2537720636


With @memoize:
get_nth_lucas_number(45)
0:00:00
2537720636

get_nth_lucas_number(100)
0:00:00
792070839848372253127


Prime factorization
print(get_prime_factors(12))
[2, 2, 3]

print(get_prime_factors(715))
[5, 11, 13]

print(get_prime_factors(20633239))
[11, 29, 71, 911]

print(get_prime_factors(get_nth_lucas_number(60)))
[2, 7, 23, 241, 2161, 20641]

print(get_prime_factors(get_nth_lucas_number(61)))
[5600748293801]

print(get_prime_factors(get_nth_lucas_number(100)))
[7, 2161, 9125201, 5738108801]
'''
