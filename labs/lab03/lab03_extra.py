from lab03 import *

# Q4
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

# Q5
def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        print (i)
    if n == 1:
        print(1)
    else:
        count_up(n - 1)
        counter(n)

# Q6
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    k = n - 1
    def helper(n, k):
        if n == 1:
            return False
        if k == 1:
            return True
        if n % k == 0:
            return False
        else:
            return helper(n, k - 1)

    return helper(n, k)




# Q7
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    if n == 1:
        return odd_term(n)
    elif n % 2 == 0:
        this = even_term(n)
        return this + interleaved_sum(n - 1, odd_term, even_term)
    else:
        this = odd_term(n)
        return this + interleaved_sum(n - 1, odd_term, even_term)



# Q8
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    count = 0

    if n // 10 == 0:
        return count

    num = []
    number = n

    while n > 0:
        num.append(n % 10)
        n = n // 10
    first = num[0]
    rest = num[1:]

    for i in range(len(rest)):
        if first + rest[i] == 10:
            count = count + 1

    return count + ten_pairs(number // 10)






